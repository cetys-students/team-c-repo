import RPi.GPIO as GPIO
from time import sleep
class LSD:
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        D0 = 5
        D1 = 6
        D2 = 13
        D3 = 19
        D4 = 26
        D5 = 12
        D6 = 16
        D7 = 20
        self.D = [D7,D6,D5,D4,D3,D2,D1,D0]
        self.Waiter = [1,1,1,1,1,1,1,1]
        for i in self.D:
            GPIO.setup(i,GPIO.OUT)
            
        self.EN = 14
        self.RW = 15
        self.RS = 18
        GPIO.setup(self.EN,GPIO.OUT)
        GPIO.setup(self.RW,GPIO.OUT)
        GPIO.setup(self.RS,GPIO.OUT)
        GPIO.output(self.EN,False)
        GPIO.output(self.RW,False)
        GPIO.output(self.RS,False)
        
        self.Flag = 21
        GPIO.setup(self.Flag,GPIO.IN)
        try:
            self.Set_Up()
            self.Two_Lines('Hello', 'World')
        except:
            print('No jala Nio')
            self.Stop()





    def Two_Lines(self,Text1,Text2):
        EN = self.EN
        RS = self.RS

        self.Two_Lines_Clear()
        
        GPIO.output(RS,False)
        Begin = [0,0,1,1,1,0,0,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Begin[i])
            #print(Begin[i])
            #print(i,j)
        
        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()
        #print("Hola")
        
        GPIO.output(RS,False)
        Turning_ON = [0,0,0,0,1,1,1,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Turning_ON[i])
            #print(i,j)

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        GPIO.output(RS,False)
        Cursor_ON = [0,0,0,0,0,1,1,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Cursor_ON[i])
            #print(i,j)

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        self.Write(Text1)

        GPIO.output(RS,False)
        Cursor_ON = [0,0,1,1,1,1,0,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Cursor_ON[i])

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        GPIO.output(RS,False)
        Cursor_ON = [1,1,0,0,0,0,0,1]
        for i,j in enumerate(self.D):
            GPIO.output(j,Cursor_ON[i])

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        self.Write(Text2)

        


    def Two_Lines_Clear(self):
        EN = self.EN
        RS = self.RS
        
        GPIO.output(RS,False)
        Clearer = [0,0,0,0,0,0,0,1]
        for i,j in enumerate(self.D):
            GPIO.output(j,Clearer[i])
            #print(i,j)

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        Clearer = [0,0,0,0,0,0,1,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Clearer[i])
            #print(i,j)

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        




    

    def Set_Up(self):
        EN = self.EN
        RS = self.RS
        
        GPIO.output(RS,False)
        Begin = [0,0,1,1,1,0,0,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Begin[i])
            #print(Begin[i])
            #print(i,j)
        
        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()
        #print("Hola")
        
        GPIO.output(RS,False)
        Turning_ON = [0,0,0,0,1,1,0,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Turning_ON[i])
            #print(i,j)

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        GPIO.output(RS,False)
        Cursor_ON = [0,0,0,0,0,1,1,0]
        for i,j in enumerate(self.D):
            GPIO.output(j,Cursor_ON[i])
            #print(i,j)

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

        self.Clear()



    def Wait(self):
        EN = self.EN
        RS = self.RS
        RW = self.RW
        
        GPIO.output(EN,False)
        
        GPIO.output(EN,True)
        sleep(0.001)
        
        GPIO.output(EN,False)
        GPIO.output(RS,False)

        
        sleep(0.00001)
        
        
        #GPIO.setup(self.D[0],GPIO.IN)
        
        
##        while GPIO.input(self.Flag) == 1:
##            GPIO.output(EN,True)
##            #sleep(0.000001)
##            GPIO.output(EN,False)
##            GPIO.setup(self.D[0],GPIO.IN)
##            #print("oie")

##        while GPIO.input(self.D[0]) != 1:
##            s = GPIO.input(self.Flag)
##        print("Pretty")

##        GPIO.setup(self.D[0],GPIO.OUT)
            
            
##            if GPIO.input(self.Flag) == 1:
##                GPIO.output(EN,False)
##                GPIO.output(RS,False)
##                GPIO.output(RW,True)
##                
##            elif GPIO.input(self.Flag) == 0:
####                print("What happen")
##                GPIO.output(EN,False)
##                break
                
##        GPIO.output(RW,False)



    def Clear(self):
        EN = self.EN
        RS = self.RS
        
        GPIO.output(RS,False)
        Clearer = [0,0,0,0,0,0,0,1]
        for i,j in enumerate(self.D):
            GPIO.output(j,Clearer[i])
            #print(i,j)

        GPIO.output(EN,True)
        sleep(0.000005)
        GPIO.output(EN,False)
        self.Wait()

    def Write(self,Double):
        self.Clear()
        Double = list(str(Double))
        for i in Double:
            Char = self.Decoder(i)
            #print(Char)
            GPIO.output(self.RS,True)
            for i,j in enumerate(self.D):
                GPIO.output(j,int(Char[i]))
            self.Wait()

    def Decoder(self,Character):
        Character = ord(Character)
        Character = '{0:08b}'.format(Character)
        return list(Character)
        
    def Stop(self):
        for i in self.D:
            #print(i)
            GPIO.output(i,False)
        GPIO.output(self.EN,False)
        GPIO.output(self.RW,False)
        GPIO.output(self.RS,False)
        GPIO.cleanup()
        
#try:
x = LSD()
##################################x.Write(2.4563)
##################################print("Nice")
##################################x.Stop()
##GPIO.cleanup()
##except:
##    print("Error or Ctrl c")
##    #x.Stop()
##    GPIO.cleanup()
