# import the necessary modules
from time import sleep
from pynq import Overlay
ps_gpio_design = Overlay("./ps_gpio_kv260.bit")
from pynq import GPIO

# assign pins
# ledswitch effectively 'increases' the number of available pins
led1 =        GPIO(GPIO.get_gpio_pin(4), 'out')
led2 =        GPIO(GPIO.get_gpio_pin(5), 'out')
led3 =        GPIO(GPIO.get_gpio_pin(6), 'out')
ledswitch =   GPIO(GPIO.get_gpio_pin(7), 'out')
count2 =      GPIO(GPIO.get_gpio_pin(0), 'out')
count3 =      GPIO(GPIO.get_gpio_pin(1), 'out')
count1 =      GPIO(GPIO.get_gpio_pin(2), 'out')
button =      GPIO(GPIO.get_gpio_pin(3), 'in')

# define constants
DELAY = 1
currentnumber = 7

# set initial led values
led1.write(0)
led2.write(0)
led3.write(0)

ledswitch.write(1)

# set initial count values
count1.write(0)
count2.write(0)
count3.write(1)

# represent current number in binary format using 'count' variables
# transitiion from one number to the next number
def changecounter(currentnumber):
    if currentnumber == 0:
        count1.write(0)
        count2.write(0)
        count3.write(0)
        sleep(0.001)
    elif currentnumber == 1:
        count1.write(1)
        count2.write(0)
        count3.write(0)
        currentnumber = 0
    elif currentnumber == 2:
        count1.write(0)
        count2.write(1)
        count3.write(0)
        currentnumber = 1
    elif currentnumber == 3:
        count1.write(1)
        count2.write(1)
        count3.write(0)
        currentnumber = 2
    elif currentnumber == 4:
        count1.write(0)
        count2.write(0)
        count3.write(1)
        currentnumber = 3
    elif currentnumber == 5:
        count1.write(1)
        count2.write(0)
        count3.write(1)
        currentnumber = 4
    elif currentnumber == 6:
        count1.write(0)
        count2.write(1)
        count3.write(1)
        currentnumber = 5
    elif currentnumber == 7:
        count1.write(1)
        count2.write(1)
        count3.write(1)
        currentnumber = 6
    return currentnumber

# the finite state machine
while(1):
    
    pressed = button.read()
    if(pressed == 1):
        currentnumber = 7
        
        # State 1
        for j in range (8):
            for i in range(1550):
                ledswitch.write(1)
                led2.write(1)
                led2.write(0)
                ledswitch.write(0)
                led3.write(1)
                led3.write(0)
            currentnumber = changecounter(currentnumber)
        currentnumber = 7
        
        # State 2
        for j in range (8):
            for i in range(1550):
                ledswitch.write(1)
                led3.write(1)
                led3.write(0)
                ledswitch.write(0)
                led1.write(1)
                led1.write(0)
            currentnumber = changecounter(currentnumber)
        currentnumber = 7
        
        # State 3
        for j in range (8):
            for i in range(1550):
                ledswitch.write(1)
                led1.write(1)
                led1.write(0)
                ledswitch.write(0)
                led1.write(1)
                led1.write(0)
            currentnumber = changecounter(currentnumber)
        currentnumber = 7
        
        # State 4
        for j in range (8):
            for i in range(1550):
                ledswitch.write(1)
                led2.write(1)
                led2.write(0)
                ledswitch.write(0)
                led2.write(1)
                led2.write(0)
            currentnumber = changecounter(currentnumber)
            
    # maintain current state and trajectory
    else:
        ledswitch.write(1)
        led2.write(1)
        led2.write(0)
        ledswitch.write(0)
        led2.write(1)
        led2.write(0)