import os
import redis
from fastapi import FastAPI
from dotenv import load_dotenv

# 建立FastAPI實體
app = FastAPI()

# 載入環境變數
load_dotenv()

# 建立redis資料庫連接
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'), decode_responses=True)

# API首頁
@app.get("/")
def read_root():
    return {"資料來源":"pico_w" }

# 計數器頁
@app.get("/counter/{c}")
def read_counter(c:int):
    counter = redis_conn.incr('test:increment', c)
    return {"Counter": counter}

# 接收pico_w傳來的資料(溫度、時間)
@app.get("/temperature/{celsius}/{time}")
def save_temperature(celsius:float, time:str):
    redis_conn.set('board:temperature', celsius)
    redis_conn.set('board:time', time)
    return 'Save successfully'

# 顯示溫度頁
@app.get("/temperature")
def read_temperature():
    celsius = redis_conn.get('board:temperature')
    time = redis_conn.get('board:time')
    return {"溫度": celsius, "時間": time}