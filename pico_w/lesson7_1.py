from machine import Pin,Timer

led25 = Pin("LED",Pin.OUT)

i = 0
def second1(t):
    global i     
    print("過1秒")
    led25.toggle()
    i = i + 1
    if(i>=3):
        t.deinit()
    
tim1 = Timer()
tim1.init(period=1000, callback=second1)
