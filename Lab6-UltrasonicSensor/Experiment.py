import RPi.GPIO as GPIO 
import Stepper as stepper
import SR04 as sr04

class Experiment:
    distances = []
    minimum = 0
    sensor = None
    stepper = None

    def __init__(self, sensorPinout, stepperPinout):
        self.sensor = sr04.SR04(sensorPinout[0], sensorPinout[1])
        self.stepper = stepper.Stepper(stepperPinout)
        self.distances = []
        self.minimum = None

    def GetSamples(self, samples):
        data = []
        for i in range(samples):
            self.stepper.RotateR(1)
            measure = self.sensor.GetDistance()

            data.append(measure)
            print(i, ". Measure: ", measure)
        return data

    def GetMinSample(self, data):
        minSample = min(data)
        return minSample

    def PerformExperiment(self, samples):
        self.distances = self.GetSamples(samples)
        self.minimum = self.GetMinSample(self.distances)

        reversedDistances = list(reversed(self.distances))
        indexMinimum = reversedDistances.index(self.minimum)
        print("\nMinimum distance:", self.minimum,
              "  Index:", self.distances.index(self.minimum),
              "  Reversed:", indexMinimum)

        self.stepper.RotateL(indexMinimum)
      
        
exp = Experiment([18, 24], [25, 8, 7, 1])
exp.PerformExperiment(512)
GPIO.cleanup()
