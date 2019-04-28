from AltIMU_v3 import AltIMUv3
from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
LEDi = 14
Buzzer = 15
GPIO.setup(LEDi,GPIO.OUT)
GPIO.setup(Buzzer,GPIO.OUT)
altimu = AltIMUv3()
altimu.enable(gyroscope=False)
GPIO.output(Buzzer,False)
try:
    while True:
        past = altimu.get_accelerometer_cal()
        current = altimu.get_accelerometer_cal()
        diffx = abs(abs(current[0])-abs(past[0]))
        diffy = abs(abs(current[1])-abs(past[1]))
        diffz = abs(abs(current[2])-abs(past[2]))
        if  diffx > 0.4 or diffy > 0.4 or diffz > 0.4:
            GPIO.output(LEDi,True)
            if (abs(current[0]) > 1.3 and  abs(current[1]) > 1.3 and abs(current[2]) > 1.3):
                GPIO.output(Buzzer,True)
                GPIO.output(LEDi,True)
                print("Fall detected!!!")
                sleep(2)
                GPIO.output(Buzzer,False)
                GPIO.output(LEDi,False)
            elif (abs(past[0]) > 1.3 and  abs(past[1]) > 1.3 and abs(past[2]) > 1.3):
                GPIO.output(Buzzer,True)
                GPIO.output(LEDi,True)
                print("Fall detected!!!")
                sleep(2)
                GPIO.output(Buzzer,False)
                GPIO.output(LEDi,False)
        else:
            GPIO.output(LEDi,False)
except:
    GPIO.cleanup()
