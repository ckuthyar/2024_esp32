from machine import Pin
import utime


led=Pin(2,Pin.OUT)
led.value(0)