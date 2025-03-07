from src.bot.handlers import save_offer, start, button
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from dotenv import load_dotenv
import os

# save environment variable
load_dotenv()

TOKEN = os.getenv("TOKEN_TELEGRAM")


def main_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, save_offer))
    app.run_polling()


if __name__ == "__main__":
    main_bot()
