from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
from bs4 import BeautifulSoup
from openai import AzureOpenAI
import logging

from config import AZURE_OPENAI_KEY, PORT, FRONT_URL, URL_CV_PDF
from handle_pdf import extract_text_from_pdf

# Configuration du logger
logging.basicConfig(filename="api.log", level=logging.INFO)


def handle_cors(app):

    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_origins=FRONT_URL,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app


app = handle_cors(FastAPI())


# Pour tester l'API
@app.get("/test/{prompt}", description="Test!")
def test():
    return "test api OK"


# Pour alimenter le chatbot avec les données du portfolio:
response1 = requests.get(FRONT_URL)
soup1 = BeautifulSoup(response1.text, "html.parser")
content1 = soup1.prettify()

text_from_pdf = extract_text_from_pdf(URL_CV_PDF)

# Concaténer les contenus
concatenated_content = content1 + text_from_pdf

# Créer un nouvel objet BeautifulSoup avec le contenu concaténé
soup = BeautifulSoup(concatenated_content, "html.parser")


# pour se connecter à l'API
@app.post("/chat/", description="output du chatbot")
async def chat(prompt):

    # Enregistrement des paramètres d'entrée
    logging.info(f"Paramètre d'entrée : {prompt}")

    client = AzureOpenAI(
        azure_endpoint="https://pauline-openai.openai.azure.com/",
        api_key=AZURE_OPENAI_KEY,
        api_version="2024-02-15-preview",
    )

    message_text = [
        {
            "role": "system",
            "content": f"You are a professionnal AI assistant who know this :{soup}.",
        },
        {"role": "user", "content": f"{prompt}"},
    ]

    completion = client.chat.completions.create(
        model="paulinegpt4",  # model = "deployment_name"
        messages=message_text,
        temperature=0.7,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None,
    )
    completion_text = completion.choices[0].message.content
    logging.info(f"Paramètre de sortie : {completion_text}")

    return completion_text


if __name__ == "__main__":
    print("Launching the back-end...")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
