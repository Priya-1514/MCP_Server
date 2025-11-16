import ccxt

class CryptoClient:
    def __init__(self):
        self.exchange = ccxt.binance()

    def get_price(self, symbol: str):
        """Get latest ticker price"""
        symbol = symbol.upper() + "/USDT"
        ticker = self.exchange.fetch_ticker(symbol)
        return {
            "symbol": symbol,
            "price": ticker["last"]
        }

    def get_history(self, symbol: str):
        """Fetch simple OHLCV data"""
        symbol = symbol.upper() + "/USDT"
        ohlcv = self.exchange.fetch_ohlcv(symbol, timeframe="1h", limit=24)

        result = []
        for item in ohlcv:
            result.append({
                "timestamp": item[0],
                "open": item[1],
                "high": item[2],
                "low": item[3],
                "close": item[4],
                "volume": item[5]
            })
        return result
