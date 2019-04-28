import RPi.GPIO as GPIO          #calling header file which helps us use GPIO’s of PI
from time import sleep                           #calling time to provide delays in program

try:
    GPIO.setmode (GPIO.BCM)
    LED = 14
    GPIO.setup(LED,GPIO.OUT)
    while True:
        x = int(input("Pon tu numero."))
        
        
        if x == 1:
            GPIO.output(LED, 1)

        elif x == 0:
            GPIO.output(LED, 0)
    #IO.setwarnings(False)           #do not show any warnings

##    IO.setmode (IO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as ‘GPIO19’)
##
##    IO.setup(19,IO.OUT)           # initialize GPIO19 as an output.
##
##    p = IO.PWM(19,100)          #GPIO19 as PWM output, with 100Hz frequency
##    p.start(0)                              #generate PWM signal with 0% duty cycle
##
##    while 1:                               #execute loop forever
##
##        for x in range (50):                          #execute loop for 50 times, x being incremented from 0 to 49.
##            p.ChangeDutyCycle(x)               #change duty cycle for varying the brightness of LED.
##            sleep(0.1)                           #sleep for 100m second
##          
##        for x in range (50):                         #execute loop for 50 times, x being incremented from 0 to 49.
##            p.ChangeDutyCycle(50-x)        #change duty cycle for changing the brightness of LED.
##            sleep(0.1)                          #sleep for 100m second
except:
    GPIO.output(LED, 0)
    GPIO.cleanup()
    print("Its done.")
    
