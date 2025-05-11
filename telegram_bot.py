import os
from dotenv import load_dotenv
from telegram import Bot

# Ortam değişkenlerini yükle (.env dosyasından)
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

bot = Bot(token=TOKEN)

def send_message(message):
    bot.send_message(chat_id=CHAT_ID, text=message)