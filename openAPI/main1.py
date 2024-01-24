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
async def read_item(date:str, address : str ,celsius:float , light:float):
    #print(f'日期:{date}')
    redis_conn.rpush("pico_w:date",date)
    #print(f'位置:{address}')
    redis_conn.hset("pico_w:address",mapping={date: address})
    #print(f'攝氏:{celsius}')
    redis_conn.hset("pico_w:celsius",mapping={date: celsius})
    #print(f'光:{light}')
    redis_conn.hset("pico_w:light",mapping={date: light})
    
    date_get = redis_conn.lrange('pico_w:date',-1,-1)[0].decode()
    address_get = redis_conn.hget('pico_w:address',date_get).decode()
    temperature_get = redis_conn.hget('pico_w:celsius',date_get).decode()
    light_get = redis_conn.hget('pico_w:light',date_get).decode()
    
    print(date_get)
    print(address_get)
    print(temperature_get)
    print(light_get)
    
    
    return {'成功'}
