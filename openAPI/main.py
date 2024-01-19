from typing import Union
from fastapi import FastAPI

import redis
from dotenv import load_dotenv
import os

load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    counter = redis_conn.incrby('testkey',1)
    return {"Counter":counter}

@app.get("/counter/{c}")  #{c} 路徑參數
def counter(c:int):
    counter1 = redis_conn.incrby('testkey',c)
    return {"Counter1":counter1}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}