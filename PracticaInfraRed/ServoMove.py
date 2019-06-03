import RPi.GPIO as GPIO    #Importamos la libreria RPi.GPIO
import time                #Importamos time para poder usar time.sleep
import cv2 
 GPIO.setmode(GPIO.BCM)  #Ponemos la Raspberry en modo BOARD
GPIO.setup(21,GPIO.OUT)    #Ponemos el pin 21 como salida  #encontrar nuevo pin para ello 
InfraRed= ##  ARRIBA
InfraRed2= ###  DERECHA
InfraRed3= ####  ABAJO 
InfraRed4=  ###### IZQUIERDA
GPIO.setup(InfraRed,GPIO.IN)
GPIO.setup(InfraRed2,GPIO.IN)
GPIO.setup(InfraRed3,GPIO.IN)
GPIO.setup(InfraRed4,GPIO.IN)
# BUSCAR LA MANERA QUE CADA VEZ QUE NO DETECTE UNO DE LLOS, EL SERVO SE MUEVA EN SU DIRECCION
# VAMOS A BUSCAR CONDICIONALES CADA VEZ QUE ENTRE COMIENZA UNA SECCUENCIA CON EL SERVO
#IF CONDICION DE 1 INFRARED

# IF CONDICION DE 2 INFRARED
#IF CONDICION DE 3 INFRARED
# IF CONDICION DE 4 INFRARED
#IF CONDICION DE 1 Y 2 INFRARED
# IF CONDICION DE 2 Y 3  INFRARED
#IF CONDICION DE 3 Y 4 INFRARED
# IF CONDICION DE 4 Y 1 INFRARED
#IF CONDICION DE  1 2 3 4 INFRARED

p = GPIO.PWM(21,50)        #Ponemos el pin 21 en modo PWM y enviamos 50 pulsos por segundo
p.start(7.5)               #Enviamos un pulso del 7.5% para centrar el servo
try:                 
    while True:      #iniciamos un loop infinito
 
        p.ChangeDutyCycle(4.5)    #Enviamos un pulso del 4.5% para girar el servo hacia la izquierda
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(10.5)   #Enviamos un pulso del 10.5% para girar el servo hacia la derecha
        time.sleep(0.5)           #pausa de medio segundo
        p.ChangeDutyCycle(7.5)    #Enviamos un pulso del 7.5% para centrar el servo de nuevo
        time.sleep(0.5)           #pausa de medio segundo
 
# TENEMOS QUE BUSCAR UNA MANERA QUE AL DETECTAR EL SENSOR, EL STEPER EMPIEXE SU MOVIMIENTO 
# UNA CONDICION POR CADA SENSOR DETECTADO
except KeyboardInterrupt:         |#Si el usuario pulsa CONTROL+C entonces...
    p.stop()                      #Detenemos el servo 
    GPIO.cleanup()                #Limpiamos los pines GPIO de la Raspberry y cerramos el script