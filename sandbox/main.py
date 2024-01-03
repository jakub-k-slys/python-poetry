from typing import Union
from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return wrapper


@singleton
class MySingleton():
    def foo(self):
        pass


def main():
    print('Hello world!!!')
    s1 = MySingleton()
    s2 = MySingleton()
    print(id(s1))
    print(id(s2))


if __name__ == "__main__":
    main()
