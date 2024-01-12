from machine import Pin
import time

start1 = time.ticks_ms()
start2 = time.ticks_ms()
start3 = time.ticks_ms()
led25 = Pin('LED',Pin.OUT)
ledStatus = False

while True:
    if time.ticks_diff(time.ticks_ms(), start1) >= 1000:
        print('過1秒')
        start1 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(), start2) >= 5000:
        print('過5秒')
        start2 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)
    if time.ticks_diff(time.ticks_ms(), start3) >= 10000:
        print('過10秒')
        start3 = time.ticks_ms()
        ledStatus = not ledStatus
        led25.value(ledStatus)

