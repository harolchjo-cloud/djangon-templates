"""
Simple runner para el bot de Telegram (polling).
Requisitos:
  pip install python-telegram-bot==20.4
Uso:
  En PowerShell:
    $env:TELEGRAM_BOT_TOKEN = "<TU_TOKEN>"
    C:/Users/harol/Desktop/proyecto/venv/Scripts/python.exe run_telegram_bot.py

No incluyas el token en el código ni lo subas a git.
"""
import os
import logging

from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram_bot.replies import get_reply

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Hola 👋 Soy el bot de RRHH. Pregunta sobre vacaciones, beneficios, horario o nómina."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text or ""
    reply = get_reply(text)
    await update.message.reply_text(reply)


def main():
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if not token:
        raise SystemExit("Define TELEGRAM_BOT_TOKEN en las variables de entorno antes de ejecutar.")

    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    logger.info("Bot iniciado (polling).")
    app.run_polling()


if __name__ == "__main__":
    main()
