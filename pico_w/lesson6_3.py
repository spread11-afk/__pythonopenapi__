from machine import Pin,Timer

led25 = Pin('LED',Pin.OUT)


def second1(t):
    print('過1秒')
    led25.toggle()
    
tim = Timer(period=1000, mode=Timer.PERIODIC, callback=second1)

