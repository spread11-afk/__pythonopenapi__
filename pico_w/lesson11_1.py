from machine import Pin
from tools import connect,reconnect
from machine import ADC,Pin,Timer,RTC
import urequests
import time
from urllib import quote



red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)

is_press = False

connect()
adc = ADC(4)     # create ADC object on ADC pin,最後一個,溫度
conversion_factor = 3.3/65535

def second1(t):
    reading_v = adc.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    celsius = 27 - (reading_v-0.706) / 0.001721
    return celsiu

while True:
    if btn.value():
        red_led.value(1)
        is_press = True
    else:
        if is_press == True:            
            now = time.ticks_ms()
            reading_v = adc.read_u16() * conversion_factor
            # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
            # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
            celsius = 27 - (reading_v-0.706) / 0.001721
            print(celsius)
            url_str = f'https://openapi-test-miif.onrender.com/pico_w/{now}?address=魚池&celsius={celsius}'
            encode_url = quote(url_str)
            print('release')
            is_press = False
            try:
                response = urequests.get(encode_url)
            except:
                print("ap出現問題")            
                reconnect()
            else:
                if response.status_code == 200:            
                    print("傳送訊息成功")
                else:
                    print("傳送失敗(make服務出問題)")
                response.close()
    red_led.value(0)
