class LowPassfilter:
    def __init__(self,measurement,bias):
        self.measurement = measurement
        self.bias = bias

    def update_measurement(self,new_measurement):
        self.measurement[0] = round((self.measurement[0]*self.bias) + (new_measurement[0]*(1-self.bias)),3)
        self.measurement[1] = round((self.measurement[1]*self.bias) + (new_measurement[1]*(1-self.bias)),3)
        self.measurement[2] = round((self.measurement[2]*self.bias) + (new_measurement[2]*(1-self.bias)),3) ##As higher the bias, lower the measurement, like only gravity
##Quick changes will be almost neglible
        return self.measurement



class HighPassfilter:
    def __init__(self,measurement,bias):
        self.measurement = measurement
        self.bias = bias

    def update_measurement(self,new_measurement):
        self.measurement[0] = round(self.measurement[0] + self.bias*(new_measurement[0]-self.measurement[0]),3)#(new_measurement[0]*(self.bias))
        self.measurement[1] = round(self.measurement[1] + self.bias*(new_measurement[1]-self.measurement[1]),3)#(new_measurement[0]*(self.bias))
        self.measurement[2] = round(self.measurement[2] + self.bias*(new_measurement[2]-self.measurement[2]),3)#(new_measurement[0]*(self.bias)) 
#Only detects fast movements.
#Estimated gravity#Reduce gyro drift.
        return self.measurement
