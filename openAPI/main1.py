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


@app.get('/pico_w/{date}')
async def read_item(date:str, address : str ,celsius:float , light_vaule:float):
    print(f'日期:{date}')
    print(f'位置:{address}')
    print(f'攝氏:{celsius}')
    print(f'光:{light_vaule}')
    return {"日期":date,"攝氏溫度":celsius}

@app.get('/pico_w/{date}')
async def read_item(date:str, address : str ,celsius:float=0.0):
    print(f'日期:{date}')
    print(f'位置:{address}')
    print(f'攝氏:{celsius}')
    return {"日期":date,"攝氏溫度":celsius}