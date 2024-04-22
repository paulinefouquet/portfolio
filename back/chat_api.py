from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import requests
from bs4 import BeautifulSoup
from openai import AzureOpenAI

from config import AZURE_OPENAI_KEY, PORT, FRONT_URL, URL_CV_PDF


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

response2 = requests.get(URL_CV_PDF)
soup2 = BeautifulSoup(response2.text, "html.parser")

# Extraire le contenu de chaque objet soup
content1 = soup1.prettify()
content2 = soup2.prettify()

# Concaténer les contenus
concatenated_content = content1 + content2

# Créer un nouvel objet BeautifulSoup avec le contenu concaténé
soup = BeautifulSoup(concatenated_content, "html.parser")


# pour se connecter à l'API
@app.post("/chat/", description="output du chatbot")
async def chat(prompt):

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
    print(f"le texte suivant a été généré: {completion_text}")

    return completion_text


if __name__ == "__main__":
    print("Launching the back-end...")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
