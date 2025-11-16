from pydantic import BaseModel

class Price(BaseModel):
    symbol: str
    price: float

class OHLC(BaseModel):
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float
