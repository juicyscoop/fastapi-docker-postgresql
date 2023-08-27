This is a demo FastAPI Application

- implemented is a simple backend for a stock-watcher app
- purpose of this project was leanrning the implementation and usage of FastAPI with uvicorn and docker
- A docker container is set up which forwards the 5432 port to 54332/tcp
- then the API is run on this endpoint at localhost:8000, connected to the database using .env  

# Installation
- from within /api

Create database:
-----
Run create script after setting up with Alembic (below)


Run database in docker container (postgres image):
-----
make run-db


Run API:
----
uvicorn src.main:app --reload




Database change management scripts are created and managed using alembic. See more at https://alembic.sqlalchemy.org/en/latest/tutorial.html

# Db Initiation
alembic init

# Db Revision
alembic revision -m "your message"

# Database Migration
alembic upgrade/downgrade head 



# Prerequisites
docker, FastAPI, yfinance, uvicorn, dotenv

