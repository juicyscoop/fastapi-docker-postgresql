
from sqlalchemy import String, Float, Date
from sqlalchemy.sql.schema import Column
from .database import Base
from sqlalchemy import Column, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base  = declarative_base()

class Stock(Base):
    __tablename__ = 'stocks'
    ticker = Column(String, nullable=False, primary_key=True)

class APPLDaily(Base):
    __tablename__ = 'aapl_daily'

    date = Column(Date, primary_key=True, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)

class TSLADaily(Base):
    __tablename__ = 'tsla_daily'

    date = Column(Date, primary_key=True, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)

class XOMDaily(Base):
    __tablename__ = 'xom_daily'

    date = Column(Date, primary_key=True, nullable=False)
    open = Column(Float, nullable=False)
    high = Column(Float, nullable=False)
    low = Column(Float, nullable=False)
    close = Column(Float, nullable=False)
    volume = Column(Float, nullable=False)