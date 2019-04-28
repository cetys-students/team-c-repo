import RPi.GPIO as GPIO
import time

class SR04:
    trigger = 0
    echo = 0

    def __init__(self, trigger, echo):
        GPIO.setmode(GPIO.BCM)
        self.trigger = trigger
        self.echo = echo
        try:
            GPIO.cleanup()
            GPIO.setup(self.trigger,GPIO.OUT)
            GPIO.setup(self.echo,GPIO.IN)
            GPIO.output(self.trigger,False)
        except:
            print("GPIO setup failed. Try again.")
            GPIO.cleanup()

    def GetDistance(self):
        startTime = 0
        stopTime = 0
        
        GPIO.output(self.trigger,True)
        time.sleep(0.00001)
        GPIO.output(self.trigger,False)

        while GPIO.input(self.echo) == 0:
            startTime = time.time()

        while GPIO.input(self.echo) == 1:
            stopTime = time.time() 

        distance = (stopTime - startTime) * 34300 / 2

        return distance   
        

#sensor = SR04(18, 24)
#while True:
#    d = sensor.GetDistance()
#    print(d)
