from machine import ADC,Timer
from tools import connect,reconnect
import time
import urequests

connect()
adc = ADC(4)     # create ADC object on ADC pin,最後一個,溫度
conversion_factor = 3.3/65535

def push_temp(t):
    
    reading_v = adc.read_u16() * conversion_factor
    # The temperature sensor measures the Vbe voltage of a biased bipolar diode, connected to the fifth ADC channel
    # Typically, Vbe = 0.706V at 27 degrees C, with a slope of -1.721mV (0.001721) per degree. 
    celsius = 27 - (reading_v-0.706) / 0.001721
    url_str = f'https://openapi-test-miif.onrender.com/temperature/{celsius}'
    try:
        response = urequests.get(url_str)            
    except:
        print("ap出現問題")            
        reconnect()
    else:
        if response.status_code == 200:
                        
            print(f"傳送訊息成功，當前溫度：{celsius}")
        else:
            print("傳送失敗(Render服務出問題)")
        response.close()
        
    
tim1 = Timer()
tim1.init(period=10000, callback=push_temp)