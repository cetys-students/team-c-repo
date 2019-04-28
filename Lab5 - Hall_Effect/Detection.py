##class Detection(self):
##    def __init__(self):
import RPi.GPIO as GPIO
import time
import threading

class Hall:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        self.Kiki = 15
        SW1 = 18
        SW2 = 23
        SW3 = 24
        SW4 = 25
        self.Switches = [SW1,SW2,SW3,SW4]
        for i in self.Switches:
            GPIO.setup(i,GPIO.IN)
        GPIO.setup(self.Kiki,GPIO.IN)

    def Detector(self):
        Kiki = self.Kiki
        SW_State = []
        try:
            while GPIO.input(Kiki) == 0:
                pass
            
            while True:
                if GPIO.input(Kiki) == 0:
                    holi = time.time()
                    while GPIO.input(Kiki) == 0:
                        pass
                    while  GPIO.input(Kiki) == 1:
##                        print("Hey")
                        pass
                            ##############if GPIO.input(Kiki) == 0:
                    timing = time.time()-holi
                    
                    for i in self.Switches:
                        SW_State.append(GPIO.input(i))
                    
                    return timing,SW_State
    ##                #LCD(timing,GPIO.input(KOM))
    ##                print(timing)
    ##                print(GPIO.input(Kiki))
                pass

        except:
            print("Something gone work.")

    def Wupdiriskup(self):
        GPIO.cleanup()

        

##Booleano = True
##
##def Display(counter):
##    global Booleano
##    while Booleano == True:
##        print("Ese")
##
##GPIO.setmode(GPIO.BCM)
##Kiki = 15
##
##GPIO.setup(Kiki,GPIO.IN)
##GPIO.setup(KOM,GPIO.IN)
####try:
##while GPIO.input(Kiki) == 0:
##    pass
##time.sleep(0.1)
##timing = 0
##
##h = 0
##t = threading.Thread(target=Display, args=(h,))
##t.start()
##
##try:
##    while True:
##        if GPIO.input(Kiki) == 0:
##            holi = time.time()
##            while GPIO.input(Kiki) == 0:
##                pass
##            while  GPIO.input(Kiki) == 1:
##                pass
##                    ##############if GPIO.input(Kiki) == 0:
##            timing = time.time()-holi
##            #LCD(timing,GPIO.input(KOM))
##            print(timing)
##            print(GPIO.input(Kiki))
##        pass
##except:
##    Booleano = False
##    t.join()
##    GPIO.cleanup()
##
