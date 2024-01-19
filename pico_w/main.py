import time
import urequests
from machine import ADC, Pin, Timer, RTC
from tools import connect, reconnect

# 連接網路
connect()

# 建立ADC實體
adc = ADC(4)

# 16進位數位訊號轉換成電壓的比率
conversion_factor = 3.3/65535

# callback函式，每10秒執行一次
def second10(t):
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree.
    
    # 計算處理器溫度
    reading_v = adc.read_u16() * conversion_factor
    celsius = 27 - (reading_v-0.706) / 0.001721
    celsius = round(celsius, 1)
    
    # 記錄時間
    rtc = RTC()
    date_tuple = rtc.datetime()
    date_str = f'{date_tuple[0]}-{date_tuple[1]}-{date_tuple[2]} {date_tuple[4]}:{date_tuple[5]}:{date_tuple[6]}'
    
    # 將溫度、時間傳送至 API server
    URL = f'https://openapi-pico.onrender.com/temperature/{celsius}/{date_str}'
    
    try:
        response = urequests.get(URL)
    except:
        print("ap出現問題")
        reconnect()
    else:
        if response.status_code == 200:            
            print("傳送訊息成功")
            print(date_str)
        else:
            print("傳送失敗")    
        response.close()

# 主程式
timer = Timer(period=1000 * 10, callback=second10)