import os
import vertexai
from vertexai.generative_models import GenerativeModel
from dotenv import load_dotenv


# load environment variable
load_dotenv()

# connexion à vertexai
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.getenv("VERTEXAI_KEY_NAME")
vertexai.init(project="offersjobmanagement-2025", location="us-central1")


async def chat_with_gemini(prompt):
    # charger le modèle
    model = GenerativeModel("gemini-2.0-flash-001")

    # envoyer une requete
    response = model.generate_content(prompt)
    response = response.candidates[0].content.parts[0].text
    return response
