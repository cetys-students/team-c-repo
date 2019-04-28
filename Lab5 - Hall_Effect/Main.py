from Potentiometer import MCP3204 as mcp
from PWM import PWM as pwm
from Detection import Hall
from LCD import LSD as lcd
from math import pi
import threading
from time import sleep

Booleano = True

def Nylon(counter):
    try:
        if Booleano == True:
            MCP = mcp(spi_channel=0)
            PWM = pwm()
            PWM.Start()

            while Booleano == True:
                Input = MCP.readAverage(0)
                PWM.Pulse(Input)
            PWM.Stop()
            MCP.close()
            print("Its done.")
                
        else:
            PWM.Stop()
            MCP.close()
            print("Its done.")
    except:
        PWM.Stop()
        MCP.close()
        print("Its done.")

h = 0
t = threading.Thread(target=Nylon, args=(h,))
t.start()


try:
    Magneto = Hall()
    LSD = lcd()
    while True:
        Toc,SW = Magneto.Detector()
        if SW[0] == 1 and SW[1] == 0 and SW[2] == 0 and SW[3] == 0:
            Convertion = str((1/Toc)*360)
            String = '%.4f deg/s' % float(Convertion)
            LSD.Write(String)

        elif SW[0] == 0 and SW[1] == 1 and SW[2] == 0 and SW[3] == 0:
            Convertion = str((1/Toc)*(2*pi))
            String = '%.4f rad/s' % float(Convertion)
            LSD.Write(String)

        elif SW[0] == 0 and SW[1] == 0 and SW[2] == 1 and SW[3] == 0:
            String = '%.4f Hz' % float(1/Toc)
            LSD.Write(String)
            
        elif SW[0] == 0 and SW[1] == 0 and SW[2] == 0 and SW[3] == 1:
            Convertion = str((1/Toc)*60)
            String = '%.4f RPM' % float(Convertion)
            LSD.Write(String)

        else:
            print('Are you okay Macflai?')
##########    while True:
##########        sleep(1)
##########        print("Hey")

except:
    Booleano = False
    t.join()
    #Magneto.Wupdiriskup()
    #LSD.Stop()
    print('Listo papi')
    

