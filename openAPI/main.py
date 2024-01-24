from typing import Union

from fastapi import FastAPI

import redis
import os
from dotenv import load_dotenv 

load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/temperature/{celsius}")
def save_temp(celsius:float):
    redis_conn.set('board:temp',celsius)
    return {"board:temp": '成功'}


@app.get("/temperature")
def get_temp():
    temp = redis_conn.get('board:temp')
    return {"當前溫度": temp}

@app.get('/pico_w/{date}')
async def read_item(date:str, address : str ,celsius:float , light:int):
    print(f'日期:{date}')
    print(f'位置:{address}')
    print(f'攝氏:{celsius}')
    print(f'光:{light}')
    return {"日期":date,"攝氏溫度":celsius}

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
