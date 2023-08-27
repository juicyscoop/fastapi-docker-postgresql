import uvicorn
import os
import yfinance as yf
from datetime import datetime, timedelta

from fastapi import FastAPI, Depends
from fastapi_sqlalchemy import DBSessionMiddleware, db

from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError

from .models import APPLDaily as ModelAPPLDaily
from .models import TSLADaily as ModelTSLADaily
from .models import XOMDaily as ModelXOMDaily
from .models import Stock as ModelStock

from .database import get_db, engine

from dotenv import load_dotenv

from .setup_logging import root

load_dotenv('.env')

ALMEBIC_VERSION = "alembic_version"
PORTFOLIO = "portfolio"
PORTFOLIO_STOCK = "portfoliostock"
STOCKS = "stocks"
WATCHLIST = "watchlist"
WATCHLIST_STOCK = "watchliststock"
TRANSACTION = "transaction"
USER = "users"
ENTITIES = "entities"

DATA_MODELS = {
    "AAPL": ModelAPPLDaily,
    "TSLA": ModelTSLADaily,
    "XOM": ModelXOMDaily,
}

def get_select_all(table):
    # TODO add filters
    return f"SELECT * FROM {table}"

def get_dates_in_range(start_date, end_date):
    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    num_days = (end_date - start_date).days + 1
    dates_in_range = [start_date + timedelta(days=i) for i in range(num_days)]
    return [date.strftime("%Y-%m-%d") for date in dates_in_range]

app = FastAPI()

# to avoid csrftokenError
app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

@app.get('/tables/')
async def get_tables(db: Session = Depends(get_db)):
    # inspector = inspect(db.engine)
    # tables = inspector.get_table_names()
    return {"tables": [i for i in engine.table_names()] }


# GET STOCKS
@app.get("/list_stocks")
async def list_stocks(db: Session = Depends(get_db)):
    result = Session.execute(db, statement=get_select_all(STOCKS))
    return { "res": [i for i in result] }

# SYNC STOCKS
@app.get("/sync_stocks")
async def sync_stocks(db: Session = Depends(get_db)):
    tables = [i for i in engine.table_names()]
    data_tables = [i for i in tables if i.endswith("_daily")]
    root.info(str(data_tables))

    for i in data_tables:
        t = i.replace("_daily", "").upper()
        db.add(ModelStock(ticker=t))

    try:
        db.commit()
    except IntegrityError as e:
        root.info("::: Data already present, update if u want to overwrite!")
   
# DOWNLOAD STOCK FROM YAHOO AND STORE IN DB
@app.get("/download_stock_daily")
async def download_stock_daily(
    ticker: str, 
    start_date: str,
    end_date: str,
    db: Session = Depends(get_db)
    ):

    if ticker not in DATA_MODELS.keys():
        root.info("::: Ticker not allowed!")
        return

    start_date = datetime.strptime(start_date, "%Y-%m-%d")
    end_date = datetime.strptime(end_date, "%Y-%m-%d")
    stock_data = yf.download(ticker, start=start_date, end=end_date)

    objects = [
        DATA_MODELS[ticker](
            date=index.strftime("%Y-%m-%d"),
            open=row["Open"],
            high=row["High"],
            low=row["Low"],
            close=row["Close"],
            volume=row["Volume"],
        )
        for index, row in stock_data.iterrows()
    ]
    
    try:
        db.bulk_save_objects(objects)
        db.commit()
    except IntegrityError as e:
        root.info("::: Data already present, update if u want to overwrite!")
   

# To run locally
if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)