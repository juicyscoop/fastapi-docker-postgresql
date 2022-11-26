from fastapi import FastAPI, Depends
from .schemas import CreateJobRequest, CreateEntityRequest
from sqlalchemy.orm import Session
from .database import get_db, Base, engine
from .models import Job, Entity, CryptoDailyDataPoint
import logging
import sys
from .yahoo import get_yahoo_data
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

app = FastAPI()


@app.post("/")
def create(details: CreateEntityRequest, db: Session = Depends(get_db)):
    to_create = Entity(
        title=details.title,
        market=details.market,
        description=details.description or None
    )
    db.add(to_create)
    db.commit()
    return {
        "success": True,
        "created_id": to_create.id
    }

@app.get("/")
def get_by_id(id: int, db: Session = Depends(get_db)):
    return db.query(Job).filter(Job.id == id).first()


@app.get("/download_yahoo")
def downloadYahooData(ticker: str, start_date: str, end_date: str, db: Session = Depends(get_db)):
    data = get_yahoo_data(ticker, start_date, end_date)
    objects = [
        CryptoDailyDataPoint(ticker=ticker, date=row['Date'], price=row['Close']) for _,row in data.iterrows() 
    ]
    db.bulk_save_objects(objects)
    db.commit()
    
    return {
        "success": True,
        "stored": len(object)
    }




@app.delete("/")
def delete(id: int, db: Session = Depends(get_db)):
    db.query(Job).filter(Job.id == id).delete()
    db.commit()
    return {
        "success": True
    }

@app.get("/list_entities")
def listEntities(db: Session = Depends(get_db)):
    query = 'SELECT * FROM entities'
    result = Session.execute(db, statement=query)
    return [i for i in result]


@app.get("/list_tables")
def listEntities(db: Session = Depends(get_db)):
    logging.info(f"ENGINE: {engine}")
    return [i for i in engine.table_names()]

@app.get("/list_crypto_daily")
def listCrypto(db: Session = Depends(get_db)):
    query = 'SELECT * FROM crypto_daily'
    result = Session.execute(db, statement=query)
    return [i for i in result]

def serialize_params(params):
    out = ""
    for key,value in params.items():
        out += f"{key} {value},\n"


# @app.post("/create_new_table")
# def createTable(table_name: str, db: Session = Depends(get_db), **kwargs):
#     if not Session.execute(db, f"SELECT TOP 1 FROM {table_name}"):
#         logging.info(f"Creating new table: {table_name}")
#         serialized_params = serialize_params(kwargs)
#         query=f"""
#         CREATE TABLE {table_name} (
#             {serialized_params}
#         );
#         """
#         Session.execute(db, statement=query)
#         db.commit()
#         return {
#             "success": True,
#         }
#     else:
#         return {
#             "success": False,
#             "code": 420,
#         }