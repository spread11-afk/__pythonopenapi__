import machine
from machine import RTC

rtc = RTC()
time = rtc.datetime()
time 
print(time)