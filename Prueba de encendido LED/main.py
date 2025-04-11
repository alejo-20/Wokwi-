#Primero llamo los modulos a trabajar
from machine import Pin
from utime import sleep

#se crea el objeto
ledRojo = Pin(5,Pin.OUT)

#Creamos el ciclo con codigo
while True:
  ledRojo.value(0)
  sleep(2)
  print ("LED Encendido")
  ledRojo.value(1)
  sleep(2)
  print ("LED Apagado")
  

