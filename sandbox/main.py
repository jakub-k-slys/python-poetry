from typing import Union
from fastapi import FastAPI
from sqlalchemy import create_engine
from os import environ

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def main():
    user = environ['POSTGRES_USER']
    password = environ['POSTGRES_PASSWORD']
    hostname = environ['POSTGRES_HOSTNAME']
    database_name = environ['POSTGRES_DB']
    psql_host = f'postgresql+psycopg2://{
        user}:{password}@{hostname}/{database_name}'
    engine = create_engine(psql_host)
    print('Hello world!!!')
    engine = engine.connect()
    with Sess

    print('Hello world!!!')


if __name__ == "__main__":
    main()
