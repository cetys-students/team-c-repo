import RPi.GPIO as GPIO
import time

class Stepper:
    pinSet = []
    rightSequence = []
    leftSequence = []

    def __init__(self, pinout):
        GPIO.setmode(GPIO.BCM)
        self.pinSet = pinout
        self.rightSequence = [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
        self.leftSequence = [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1, 0, 0], [1, 0, 0, 0]]
        try:
            for i in range(len(self.pinSet)):
                    GPIO.setup(self.pinSet[i], GPIO.OUT)
                    GPIO.output(self.pinSet[i], 0)
        except:
            print("GPIO setup failed. Try again.")
            GPIO.cleanup()

    def RotateR(self, steps, delay=0.01):
        for i in range(steps):
            for j in self.rightSequence:
                GPIO.output(self.pinSet[0],j[0])
                GPIO.output(self.pinSet[1],j[1])
                GPIO.output(self.pinSet[2],j[2])
                GPIO.output(self.pinSet[3],j[3])
                time.sleep(delay)

    def RotateL(self, steps, delay=0.01):
        for i in range(steps):
            for j in self.leftSequence:
                GPIO.output(self.pinSet[0],j[0])
                GPIO.output(self.pinSet[1],j[1])
                GPIO.output(self.pinSet[2],j[2])
                GPIO.output(self.pinSet[3],j[3])
                time.sleep(delay)
       
#s = Stepper([25, 8, 7, 1])
#s.RotateR(512)
#s.RotateL(512)

    


