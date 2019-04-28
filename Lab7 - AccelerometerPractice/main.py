from AltIMU_v3 import AltIMUv3
from time import sleep
from GyroLowHigh import LowPassfilter as LP
from GyroLowHigh import HighPassfilter as HP
from Integral import Integration
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
External = 14
Position = 15
GPIO.setup(External,GPIO.OUT)
GPIO.setup(Position,GPIO.OUT)
altimu = AltIMUv3()
altimu.enable(gyroscope=False)
LPf = LP(altimu.get_accelerometer_average(average=5),0.88)
HPf = HP(altimu.get_accelerometer_average(average=5),0.30)

k = 0

def Comparation(Sample1,Sample2):
    global External
    global altimu
    global HPf

    global Position

    
    
    
    RestaX = round(abs(abs(Sample1[0])-abs(Sample2[0])),3)
    RestaY = round(abs(abs(Sample1[1])-abs(Sample2[1])),3)
    RestaZ = round(abs(abs(Sample1[2])-abs(Sample2[2])),3)
    if RestaX > 0.003 or RestaY > 0.003 or RestaZ > 0.003:
        if RestaX > 0.001 and RestaY > 0.001:
            GPIO.output(External,False)
            GPIO.output(Position,False)
            
        elif RestaY > 0.002 and RestaZ > 0.002:
            GPIO.output(External,False)
            GPIO.output(Position,False)
            
        elif RestaX > 0.002 and RestaZ > 0.002:
            GPIO.output(External,False)
            GPIO.output(Position,False)
            
        else:
            GPIO.output(External,True)
            oie = altimu.get_accelerometer_average(average=5)
            oieHP = HPf.update_measurement(oie)
            print(oieHP)
            Ubicacion(-0.01,-0.011,-0.87,oieHP)

            

    else:
        GPIO.output(External,True)
        oie = altimu.get_accelerometer_average(average=5)
        oieHP = HPf.update_measurement(oie)
        print(oieHP)
        Ubicacion(-0.01,-0.011,-0.87,oieHP)

    

def Ubicacion(LimX,LimY,LimZ,Actual):
    global Position
    RestaX = round(abs(abs(LimX)-abs(Actual[0])),3)
    RestaY = round(abs(abs(LimY)-abs(Actual[1])),3)
    RestaZ = round(abs(abs(LimZ)-abs(Actual[2])),3)
    if RestaX > 0.01 or RestaY > 0.01 or RestaZ > 0.01:
        GPIO.output(Position,False)

    else:
        GPIO.output(Position,True)
        

try:
    while True:
        k += 1
        accel = altimu.get_accelerometer_average(average=5)
        accelLP = LPf.update_measurement(accel) #altimu.get_accelerometer_cal()

        if k == 1:
            Aceleracion1 = [float(accelLP[0]),float(accelLP[1]),float(accelLP[2])]

        elif k == 2:
            Aceleracion2 = [float(accelLP[0]),float(accelLP[1]),float(accelLP[2])]
            Comparation(Aceleracion1,Aceleracion2)
            k = 0

except:
    GPIO.cleanup()
    print('Listo.')
    
    
