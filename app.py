import time
from datetime import datetime
from signal_logic import get_signal
from telegram_bot import send_message

semboller = {
    "XAUUSD": "GOLD",
    "NDX": "US100",
    "GDAXI": "GER40"
}

def is_time_valid():
    now = datetime.now()
    return 9 <= now.hour < 24

def main():
    while True:
        if is_time_valid():
            for sembol, isim in semboller.items():
                signal = get_signal(symbol=sembol, interval="15m")
                mesaj = f"{isim} 15dk sinyalin: {signal}"
                send_message(mesaj)
                time.sleep(3)  # Telegram'da flood yememek için kısa bekleme
        else:
            print("Zaman dışında. Bekleniyor...")

        time.sleep(60 * 60)  # Her 60 dakikada bir çalış

if name == "__main__":
    main()
