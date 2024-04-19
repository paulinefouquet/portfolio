from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json
import requests
from bs4 import BeautifulSoup

from config import EDENAI_KEY, PORT, FRONT_URL

# Pour que le chatbot fonctionne : il faut saisir une key de l'API EdenAI
headers = {"Authorization": EDENAI_KEY}
url = "https://api.edenai.run/v2/text/chat"
provider = "openai"

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
response = requests.get(FRONT_URL)
soup = BeautifulSoup(response.text, "html.parser")

# pour se connecter à l'API
@app.post("/chat/", description="output du chatbot")
async def chat(prompt):
    payload = {
        "providers": provider,
        "text": "",
        "chatbot_global_action": f"Act as an professional assistant with this :{soup}",
        "previous_history": [],
        "temperature": 0.8,
        "max_tokens": 200,
        "fallback_providers": "",
    }
    payload["text"] = prompt

    response = requests.post(url, json=payload, headers=headers)

    print(f"la question suivante a été posée: {prompt}")

    result = json.loads(response.text)[provider]
    print(f"le texte suivant a été généré: {result['generated_text']}")
    return result["generated_text"]


if __name__ == "__main__":
    print("Launching the back-end...")
    uvicorn.run(app, host="localhost", port=PORT)
