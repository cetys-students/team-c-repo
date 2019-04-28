import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
import RPi.GPIO as GPIO
from time import sleep                           #calling time to provide delays in program

class PWM:

    def __init__(self):
        try:
            GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
            GPIO.setup(14,GPIO.OUT)           # initialize GPIO19 as an output.
            self.p = GPIO.PWM(14,100)          #GPIO14 as PWM output, with 100Hz frequency

        except:
            print("Its done.")
            GPIO.cleanup()

    def Start(self):
        self.p.start(0)

    def Stop(self):
        self.p.stop()
        GPIO.cleanup()

    def Comparator(self,Input):
        i = 1
        ADC = 40.80
        Max = ADC*100
        while True:
            if Input > ADC*i:
                if Input < Max:
                    i += 1

                elif Input > Max:
                    return 100
                
            elif Input < ADC*i:
                if Input < 20:
                    return 0
                return i

    def Pulse(self, Input):
        c = self.Comparator(Input)
        self.p.ChangeDutyCycle(c)
        #print(Input,c)

    
        
##        try:
##            while True:                               #execute loop forever
##                for x in range (100):                          #execute loop for 50 times, x being incremented from 0 to 49.
##                    p.ChangeDutyCycle(x)               #change duty cycle for varying the brightness of LED.
##                    sleep(0.1)                           #sleep for 100m second
##                  
##                for x in range (100):                         #execute loop for 50 times, x being incremented from 0 to 49.
##                    p.ChangeDutyCycle(100-x)        #change duty cycle for changing the brightness of LED.
##                    sleep(0.1)                          #sleep for 100m second
##        except:
##            print("Its done.")
##            GPIO.cleanup()
