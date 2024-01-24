from machine import Pin
from tools import connect,reconnect
from machine import ADC,Pin,Timer,RTC
import urequests
import time



red_led = Pin(15,mode=Pin.OUT)
btn = Pin(14,mode=Pin.PULL_DOWN)

is_press = False

#connect()
adc = ADC(4)     # create ADC object on ADC pin,最後一個,溫度
conversion_factor = 3.3/65535

def second1():
    reading_v = adc.read_u16() * conversion_factor
    celsius = 27 - (reading_v-0.706) / 0.001721
    return celsius

def gettime():
    tuple_time = time.localtime()
    time_str = f'{tuple_time[0]}-{tuple_time[1]}-{tuple_time[2]}　{tuple_time[3]}：{tuple_time[4]}：{tuple_time[5]}'
    return time_str

def getLight():
    adc = ADC(Pin(28))
    light_vaule = adc.read_u16()
    return light_vaule
    

while True:
    if btn.value():
        red_led.value(1)
        is_press = True
    else:
        if is_press == True:
            time.sleep_ms(50)
            if is_press == True: 
                now = time.ticks_ms()
                reading_v = adc.read_u16() * conversion_factor
                celsius = second1()
                #celsius = 27 - (reading_v-0.706) / 0.001721
                print(celsius)
                time_str = gettime()
                print(time_str)
                print(getLight())
                #url_str = f'https://openapi-test-miif.onrender.com/pico_w/{now}?address=魚池&celsius={celsius}'
                print('release')
                red_led.value(1)
                is_press = False
                '''
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
                '''
            red_led.value(0)
