def definite_integral(samples, sampling_period=1,TimeFactor):
    #DEFINIMOD LA ECUACION PARA LA Trapezoidal Integration 
    upper_limit = samples[-1]
    print(samples.index(samples[-1]))
    lower_limit = samples[0]
   

    #tratando de aplicar la formula, veremos si funciona el for que vaya incrementando de acuerdo al rango que se pide del sampling period
    #Una formula para los primer y ultimo valor ya que estos no estan  multiplicados
    Formula1 =  (sampling_period/2) * (lower_limit +  upper_limit)
    Formula2 = 0
    print("Valor de la formuala 1 carnal", Formula1)
    print('Samples[-1]: %i' % samples[-1])
    for Values in range(samples.index(samples[1]), samples.index(samples[-1]), sampling_period):
    	print(Values)
    	summ = (sampling_period/2) * (2 * samples[Values])
    	Formula2 += summ
    	FinalResult = Formula2 +  Formula1
    	print(FinalResult)

x = [0,1,4,9,16,25,36,49,64]
#x = [0,1.5,2.5,3.5,4.5,5.5]
definite_integral(x)
