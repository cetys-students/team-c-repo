import RPi.GPIO as GPIO
import time
import LCD_I2C 

isDetecting = False
timeCounter = 0
peopleCounter = 0

GPIO.cleanup()

pinout = [6, 13, 19, 26] # output to mux 

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN) # PIR input

lcd = LCD_I2C.lcd()

for pin in pinout:
    GPIO.setup(pin, GPIO.OUT) # configure output pins

def to_binary(value):
    binary = []
    while value != 0:
        bit = int(value % 2)
        binary.append(bit)
        value = int(value / 2)
    binary.reverse()
    for dummy in range(4-len(binary)):
        binary.insert(0, 0)
    return binary

def updateTimer(seconds): 
    global pinout
    binary = to_binary(seconds) # create the binary equivalent to the number of seconds
    for i in range(4):
        GPIO.output(pinout[i], binary[i])

try:
    time.sleep(4) # to stabilize sensor    
    while True:
        if GPIO.input(23): # Detected
            print("Motion detected")
            isDetecting = True

            peopleCounter += 1
            lcd.lcd_display_string(string="People detected:",line=1,pos=0)
            lcd.lcd_display_string(string=str(peopleCounter),line=2,pos=0)

            while isDetecting:
                if not GPIO.input(23): # if not input is detected, reset the timer and timeCounter to zero
                    isDetecting = False
                    timeCounter = 0
                    updateTimer(timeCounter)
                    break

                if timeCounter < 10: # increase timeCounter while is minor to 10, otherwise reset to 0
                    timeCounter += 1
                    updateTimer(timeCounter)
                else:
                    timeCounter = 0
                    updateTimer(timeCounter)

                time.sleep(1)
            
            time.sleep(0.1) # loop delay
        else:
            isDetecting = False
            time.sleep(0.1) # loop delay
except:
    GPIO.cleanup()
