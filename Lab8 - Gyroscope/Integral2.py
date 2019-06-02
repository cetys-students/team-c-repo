import time

class Integration:
    
    def __init__(self):
        self.running_result_Positive = 0
        self.running_result_Negative = 0
        self.Timing = 0

    def definite_integral(self,samples, sampling_period=1,time_factor=1):
        final_result = 0
        #DEFINIMOD LA ECUACION PARA LA Trapezoidal Integration 
        upper_limit = samples[-1]
        #print(samples.index(samples[-1]))
        lower_limit = samples[0]
       
        #tratando de aplicar la formula, veremos si funciona el for que vaya incrementando de acuerdo al rango que se pide del sampling period
        #Una formula para los primer y ultimo valor ya que estos no estan  multiplicados
        first_value =  (time_factor*sampling_period/2) * (lower_limit +  upper_limit)
        second_value = 0
        #print('Samples[-1]: %i' % samples[-1])
        for Values in range(samples.index(samples[1]), samples.index(samples[-1]), sampling_period):
            #print(Values)
            summ = (time_factor*sampling_period/2) * (2 * samples[Values])
            second_value += summ
            final_result = second_value +  first_value
            
            #print(FinalResult)
        return final_result

##    def running_integral(self, samples, sampling_period=1, time_factor=1):
##        
##        final_result = self.definite_integral(samples, sampling_period=1, time_factor)
##        self.running_result += final_result
##        return self.running_result

    def running_integral(self, samples, time_lapse=1, sign=None):
        timing = (time_lapse-self.Timing)/len(samples)
        
        insulting = self.definite_integral(samples, time_factor=timing)
        
        if sign == 1:
            self.running_result_Positive += insulting
            RONIN = self.running_result_Positive
            #print(RONIN)
        elif sign == 2:
            self.running_result_Negative += insulting
            RONIN = self.running_result_Negative
            #print(RONIN)
            
        self.Timing = time_lapse
##        print(time_lapse)
        return RONIN

    def clear(self):
        self.running_result_Positive = 0
        self.running_result_Negative = 0
        self.Timing = 0
 


##j = Integration()
##
##x = [0,1,4,9,16,25,36,49]
###x = [0,1.5,2.5,3.5,4.5,5.5]
##j.definite_integral(x)
##j.running_integral(x)

'''
Time = ????
Grados = ????
'''
