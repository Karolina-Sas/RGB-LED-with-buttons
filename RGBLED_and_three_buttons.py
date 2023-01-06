import utime
import machine

r_LED=machine.Pin(15,machine.Pin.OUT)
g_LED=machine.Pin(14,machine.Pin.OUT)
b_LED=machine.Pin(13,machine.Pin.OUT)

button1=machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_DOWN)
button2=machine.Pin(11, machine.Pin.IN, machine.Pin.PULL_DOWN)
button3=machine.Pin(10, machine.Pin.IN, machine.Pin.PULL_DOWN)
 
 

while True:
    if button1.value()==1:
        r_LED.value(0)
        g_LED.value(0)
        b_LED.value(1)
        
    elif button2.value()==1:
        r_LED.value(0)
        g_LED.value(1)
        b_LED.value(0)
        
    elif button3.value()==1:
        r_LED.value(1)
        g_LED.value(0)
        b_LED.value(0)
        
    elif button3.value()==1 and button3.value()==1:
        r_LED.value(1)
        g_LED.value(1)
        b_LED.value(0)
    elif button2.value()==1 and button1.value()==1:
        r_LED.value(1)
        g_LED.value(0)
        b_LED.value(1)
        
    else:
        r_LED.value(0)
        g_LED.value(0)
        b_LED.value(0)
        
            
        
        