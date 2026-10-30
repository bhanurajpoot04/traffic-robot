# Activity 1 - Single LED Blink (Wokwi, ESP32-S3, MicroPython)
# Circuit: GPIO 2 -> 220 ohm resistor -> LED anode (+), LED cathode (-) -> GND
from machine import Pin
import time

# GPIO 2 ko output mode mein set karo
led = Pin(2, Pin.OUT)

print('LED Blink start!')

while True:
    led.value(1)      # LED ON
    print('ON')
    time.sleep(1)     # 1 second ruko
    led.value(0)      # LED OFF
    print('OFF')
    time.sleep(1)
