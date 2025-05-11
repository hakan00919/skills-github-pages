import yfinance as yf
import pandas as pd
import ta

def get_signal(symbol="XAUUSD", interval="15m"):
    try:
        data = yf.download(tickers=symbol, interval=interval, period="2d")

        if data.empty:
            return "Veri alınamadı."

        # Göstergeleri hesapla
        data["rsi"] = ta.momentum.RSIIndicator(data["Close"]).rsi()
        data["ema20"] = ta.trend.EMAIndicator(data["Close"], window=20).ema_indicator()
        data["ema50"] = ta.trend.EMAIndicator(data["Close"], window=50).ema_indicator()

        last = data.iloc[-1]

        # Sinyal üretme mantığı (örnek)
        if last["rsi"] < 30 and last["ema20"] > last["ema50"]:
            return "AL"
        elif last["rsi"] > 70 and last["ema20"] < last["ema50"]:
            return "SAT"
        else:
            return "NÖTR"

    except Exception as e:
        return f"Hata: {e}"