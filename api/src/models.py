
from sqlalchemy import Integer, String, Float
from sqlalchemy.sql.schema import Column
from .database import Base


class Job(Base):
    __tablename__ = 'jobs'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    description = Column(String, nullable=False)


class Entity(Base):
    __tablename__ = 'entities'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    market = Column(String, nullable=False)
    description = Column(String, nullable=True)

class CryptoDailyDataPoint(Base):
    __tablename__ = 'crypto_daily'

    id = Column(Integer, primary_key=True)
    ticker = Column(String, nullable=False)
    date = Column(String, nullable=False)
    price = Column(Float, nullable=False)