from fastapi import FastAPI
from app.services.ccxt_client import CryptoClient
from app.cache import Cache
from app.exceptions import APIError

app = FastAPI()
client = CryptoClient()
cache = Cache()

@app.get("/")
def home():
    return {"message": "Crypto MCP Server running"}

@app.get("/price/{symbol}")
def get_price(symbol: str):
    cached = cache.get(symbol)
    if cached:
        return cached

    try:
        data = client.get_price(symbol)
        cache.set(symbol, data)
        return data
    except Exception as e:
        raise APIError(str(e))

@app.get("/history/{symbol}")
def get_history(symbol: str):
    try:
        data = client.get_history(symbol)
        return data
    except Exception as e:
        raise APIError(str(e))
