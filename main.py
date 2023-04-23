#importing necessary libraries

from typing import List
from fastapi import FastAPI, HTTPException
from models import Trade, TradeDetails
import datetime as dt



app = FastAPI()

#database
trade_database = [
    Trade(
    assetClass = "Bond",
    counterparty = None,
    instrumentId = "TSLA",
    instrumentName = "Telsa car",
    tradeDateTime = dt.datetime(2023, 4, 20, 10, 43, 0),
    tradeDetails = TradeDetails(buySellIndicator = "BUY", price = 2000.0, quantity = 1),
    tradeId = "123456",
    trader = "Sravan Sunkara"
    ),
    Trade(
    assetClass = "Equity",
    counterparty = None,
    instrumentId = "AAPL",
    instrumentName = "Apple watch",
    tradeDateTime = dt.datetime(2023, 4, 21, 11, 34, 0),
    tradeDetails = TradeDetails(buySellIndicator = "SELL", price = 200.0, quantity = 5),
    tradeId = "789012",
    trader = "Lithin"
    ),
    Trade(
    assetClass = "FX",
    counterparty = None,
    instrumentId = "AMZN",
    instrumentName = "Amazon alexa",
    tradeDateTime = dt.datetime(2023, 4, 22, 9, 33, 0),
    tradeDetails = TradeDetails(buySellIndicator = "BUY", price = 1000.0, quantity = 30),
    tradeId = "345678",
    trader = "Datta"
    )
]
   
#testing
@app.get("/")
def root():
    return {"Hello": "Trader!"}

#retrieving a list of Trades
@app.get("/api/v1/traders", response_model=List[Trade])
def fetch_traders():
    return trade_database

#retrieving a single Trade by ID
@app.get("/api/v1/traders/{trade_id},  response_model=Trade")
def fetch_trader_id(trade_id : int):
    for trade in trade_database:
        if trade.tradeId == trade_id:
            return trade
    raise HTTPException(
        status_code= 404,
        detail=f"Trader with id: {trade_id} does not exists"
    )
#searching against Trades
#filtering Trades