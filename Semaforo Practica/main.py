#Se importan las librerias o modulos

from machine import Pin
from utime import sleep

#Crear los objetos 
led_verde = Pin(15, Pin.OUT)
led_amarillo = Pin(2, Pin.OUT)
led_rojo = Pin(4, Pin.OUT)

#Comenzar el ciclo en codigo

while True: 
    led_rojo.value(1)
    print ("Pare")
    sleep(2)
    led_rojo.value(0)
    print ("detengase")

    led_amarillo.value(1)
    print ("alistese")
    sleep(2)
    led_amarillo.value(0)
    print ("espere")

    led_verde.value(1)
    print ("adelante")
    sleep(2)
    led_verde.value(0)
    print ("siga")
