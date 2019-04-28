import RPi.GPIO as GPIO
Hall = 15
GPIO.setup(Hall,GPIO.IN)

while GPIO.input(Hall) == 
