from machine import Pin
import time

led25 = Pin('LED', Pin.OUT)
ledStatus = False

# 定義計時器間隔列表
intervals = [1000, 5000, 10000]
starts = [time.ticks_ms()] * len(intervals)

while True:
    for i, interval in enumerate(intervals):
        if time.ticks_diff(time.ticks_ms(), starts[i]) >= interval:
            print(f'過{interval//1000}秒')
            starts[i] = time.ticks_ms()
            ledStatus = not ledStatus
            led25.value(ledStatus)
