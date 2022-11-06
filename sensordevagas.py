from machine import Pin
from time import sleep

LED = Pin(28, Pin.OUT)
PIR_sensor = Pin(27, Pin.IN, Pin.PULL_UP)
LED.high()
sleep(1)

while True:
    print(PIR_sensor.value())
    if PIR_sensor.value() == 0:
        print("Vaga Disponivel!")
        LED.high()
        sleep(2)
    else:
        print("Vaga Ocupada!")
        LED.low()
        sleep(10)   
