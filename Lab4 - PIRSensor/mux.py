import RPi.GPIO as GPIO
import time

pout = [6, 13, 19, 26]

GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

for pin in pout:
    GPIO.setup(pin, GPIO.OUT)

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

counter = 0
while True:
    if counter == 11:
        counter = 0
        binary = to_binary(counter)
        for i in range(0, 4):
            GPIO.output(pout[i], binary[i])
        time.sleep(1)
        counter += 1
    else:
        binary = to_binary(counter)
        for i in range(0, 4):
            GPIO.output(pout[i], binary[i])
        time.sleep(1)
        counter += 1
        
    
