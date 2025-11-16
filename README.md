MCP Crypto Market Data Server

This project is a Python-based MCP server that provides real-time and historical cryptocurrency market data. The server is built using FastAPI, and it fetches data from major exchanges through CCXT. The goal of this project was to understand how MCP servers work, how to interact with crypto APIs, and how to build a clean, modular Python backend.

*88Why I Built It

The assignment required a small MCP server with features like:

endpoints to fetch data

support for real-time updates

historical queries

caching

structured code

test coverage

I kept the code simple so anyone can read it easily, while still keeping the structure clean.

*Features Implemented

Live price lookup

Historical OHLCV (1 hour candles, last 24 hours)

Lightweight caching

Error handling

Tests using pytest

Clean folder structure

**Project Structure

mcp-server/
├─ app/
│  ├─ main.py
│  ├─ services/ccxt_client.py
│  ├─ cache.py
│  ├─ models.py
│  └─ exceptions.py
├─ tests/test_api.py
├─ requirements.txt
└─ README.md

***Technologies Used

FastAPI

CCXT

Pytest

Uvicorn

Python

**Endpoints

1. Root
GET /
Response:
{ "message": "Crypto MCP Server running" }

2. Latest Price
GET /price/{symbol}
Example: /price/BTC

3. Historical OHLCV
GET /history/{symbol}
Example: /history/ETH

***How to Run

1. Install dependencies
pip install -r requirements.txt

2. Start the server
uvicorn app.main:app --reload

3. Test API
http://127.0.0.1:8000/price/BTC
http://127.0.0.1:8000/history/ETH

4. Run Tests
pytest

***Assumptions

Binance is the default exchange.

Symbols assumed to trade against USDT.

Cache expiry: 10 seconds.

Historical timeframe: 1h.

***Possible Improvements

Support multiple exchanges

WebSocket streaming

Redis caching

More detailed tests

Environment variables

Conclusion

This project meets the MCP assignment requirements with clear Python code, real-time crypto data, historical queries, caching, structured layout, and test coverage.