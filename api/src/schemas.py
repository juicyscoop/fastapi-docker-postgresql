from pydantic import BaseModel

class CreateJobRequest(BaseModel):
    title: str
    description: str

class CreateEntityRequest(BaseModel):
    title: str 
    market: str
    description: str = None

class CreateCryptoDailyDataPointRequest(BaseModel):
    ticker: str 
    date: str
    price: str