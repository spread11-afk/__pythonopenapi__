from machine import Pin
import time

start1 = time.ticks_ms()
start2 = time.ticks_ms()
start3 = time.ticks_ms()
led25 = Pin('LED',Pin.OUT)
ledStatus = False

while True:
    for start,sec,text in [(start1,1000,'1sec'),(start2,5000,'5sec'),(start3,10000,'10sec')]:
        if time.ticks_diff(time.ticks_ms(), start) >= sec:
            print(start)
            start = time.ticks_ms()
            ledStatus = not ledStatus
            led25.value(ledStatus)


