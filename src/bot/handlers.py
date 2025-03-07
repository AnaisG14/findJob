from pathlib import Path
import json
from telegram.ext import CallbackContext, ContextTypes
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from src.services.gemini import chat_with_gemini
from src.services.google_sheets import GoogleSheetOfferJobManager
from src.services.models import OfferJob


# Dir to save message
TEXT_DIR = Path("text_messages")
TEXT_DIR.mkdir(exist_ok=True)

# sujets possibles

SUBJECTS = {
    'save_job': "Enregistrer une annonce",
}


async def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton(SUBJECTS['save_job'], callback_data="save_job")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Que veux-tu faire ?", reply_markup=reply_markup)


# Étape 2 : Gestion du choix
async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    # Vérifier si l'utilisateur a bien choisi une option
    if query.data in SUBJECTS:
        context.user_data["subject"] = query.data
        message = "Allons-y !\n"
        if query.data == 'save_job':
            message += "Copie l'annonce d'emploi ici"
        await query.edit_message_text(message)
    else:
        await query.edit_message_text("Choix invalide. Essaie encore.")


async def save_offer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    subject = context.user_data.get('subject')
    if not subject:
        await update.message.reply_text("Choisis d'abord un sujet")

    text = update.message.text
    if not text:
        return

    prompt = """Peux-tu me transformer cette offre d'emploi en un JSON valide, avec les clés suivantes :
        "nom_de_l_entreprise", "intitule_du_poste", "lieu", "teletravail",
        "description_des_missions", "competences_requises", "type_de_contrat",
        "date_de_l_offre", "lien_vers_l_offre", "info_entreprise".

        Format JSON uniquement, sans texte additionnel.
    """

    message = f"{prompt}\n{text}"
    await update.message.reply_text("Envoi à gemini en cours...")
    response = await chat_with_gemini(message)
    # Suppression des backticks et du tag "json" si présent
    clean_json = response.strip("```json").strip("```").strip()

    # Conversion en dictionnaire Python
    offre_emploi = json.loads(clean_json)

    # Envoi le json et les infos pour avoir un message pour postuler à l'offre
    prompt = f"""Peux-tu me rédiger un message pour postuler à cette offre:\n {offre_emploi}"""
    message = await chat_with_gemini(prompt)

    # créer une liste
    offre_emploi = list(offre_emploi.values())
    offre_emploi.append(message)

    await update.message.reply_text("Enregistrement dans suivi offres emploi...")
    managerSheet = GoogleSheetOfferJobManager()
    offer_job = OfferJob.from_list(offre_emploi)
    managerSheet.add_offer(offer_job)
    await update.message.reply_text("Traitement terminé, retrouvez l'annonce dans le fichier suivi offres emploi")
