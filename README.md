This is a demo FastAPI Application

- implemented is a simple backend for a stock-watcher app
- purpose of this project was leanrning the implementation and usgae of FastAPI with uvicorn and docker


# Installation
- from within /api

Install database:
-----
make run-db


Run Database:
----
uvicorn src.main:app --reload


Install React dependencies:
-----
yarn install


Run React app:
------
yarn run



Database change management scripts are created and managed using alembic. See more at https://alembic.sqlalchemy.org/en/latest/tutorial.html

# Db Initiation
alembic init

# Db Revision
alembic revision -m "your message"

# Database Migration
alembic upgrade/downgrade head 

