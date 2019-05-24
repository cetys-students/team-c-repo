from AltIMU_v3 import AltIMUv3
from time import sleep
from GyroLowHigh import LowPassfilter as LP
from GyroLowHigh import HighPassfilter as HP
from Integral import Integration
import RPi.GPIO as GPIO
from time import time
from Integral2 import Integration

GPIO.setmode(GPIO.BCM)
XMeasure = 17
YMeasure = 27
ZMeasure = 22
Button_Pressed = 0

GPIO.setup(XMeasure,GPIO.IN)
GPIO.setup(YMeasure,GPIO.IN)
GPIO.setup(ZMeasure,GPIO.IN)
GPIO.setup(Button_Pressed,GPIO.IN)


GPIO.input(XMeasure)
GPIO.input(YMeasure)
GPIO.input(ZMeasure)
GPIO.input(Button_Pressed)

Integral_Corrida = Integration()
Positive = 0
Negative = 0
Boolean = False

def Axis_Rotation(Axis,Altimu,Axe):
    global Button_Pressed
    global Integral_Corrida
    global Positive
    global Negative
    global Yastuvo
    
    if GPIO.input(Button_Pressed) == True:
        First = time()
        while GPIO.input(Button_Pressed) == True:

            Axel = Altimu.get_regulated_value(Holi)
            if abs(Axel[Axis]) > 2:
##                Texto1 = '%s Positive: %.3f' % (Axe,Positive)
##                Texto2 = '%s Negative: %.3f' % (Axe,Negative)
##                print(Texto1)
##                print(Texto2)
                ZUKI = []
                while Axel[Axis] > 0:
                    ZUKI.append(Axel[Axis])
                    Axel = Altimu.get_regulated_value(Holi)
                    if len(ZUKI) > 10:
                        Positive = Integral_Corrida.running_integral(ZUKI,time_lapse=time()-First,sign=1)
                        print('%s Positive: %.3f' % (Axe,Positive))
                        ZUKI = []
                if len(ZUKI) > 3:
                    Positive = Integral_Corrida.running_integral(ZUKI,time_lapse=time()-First,sign=1)
                    print('%s Positive: %.3f' % (Axe,Positive))
                ZUKI = []

                while Axel[Axis] < 0:
                    ZUKI.append(Axel[Axis])
                    Axel = Altimu.get_regulated_value(Holi)
                    if len(ZUKI) > 10:
                        Negative = Integral_Corrida.running_integral(ZUKI,time_lapse=time()-First,sign=2)
                        print('%s Negative: %.3f' % (Axe,Negative))
                        ZUKI = []
                if len(ZUKI) > 4:
                    Negative = Integral_Corrida.running_integral(ZUKI,time_lapse=time()-First,sign=2)
                    print('%s Negative: %.3f' % (Axe,Negative))
                ZUKI = []                
            else:
                Integral_Corrida.Timing = time()-First
                pass
    else:
        Positive = 0
        Negative = 0
        Integral_Corrida.clear()
        pass

altimu = AltIMUv3()
altimu.enable(accelerometer=False)
Holi = altimu.get_bias_gyro()

while True:
    if GPIO.input(XMeasure) == True and GPIO.input(YMeasure) == False and GPIO.input(ZMeasure) == False:
        Axis_Rotation(0,altimu,'X')


    elif GPIO.input(XMeasure) == False and GPIO.input(YMeasure) == True and GPIO.input(ZMeasure) == False:
        Axis_Rotation(1,altimu,'Y')


    elif GPIO.input(XMeasure) == False and GPIO.input(YMeasure) == False and GPIO.input(ZMeasure) == True:
        Axis_Rotation(2,altimu,'Z')

