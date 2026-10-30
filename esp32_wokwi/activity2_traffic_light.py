# Activity 2 - Traffic Light Simulation (Red / Yellow / Green)
# Circuit: GPIO 4 -> Green LED, GPIO 5 -> Yellow LED, GPIO 2 -> Red LED
#          (each through a 220 ohm resistor), all LED cathodes -> GND
from machine import Pin
import time

green = Pin(4, Pin.OUT)
yellow = Pin(5, Pin.OUT)
red = Pin(2, Pin.OUT)

# Startup safety: sab band karo
green.value(0)
yellow.value(0)
red.value(0)

print('Traffic Light ready!')

while True:
    # GREEN - 5 seconds
    print('GREEN - Gaadiyaan chal sakti hain!')
    green.value(1)
    yellow.value(0)
    red.value(0)
    time.sleep(5)

    # YELLOW - 2 seconds
    print('YELLOW - Slow down karo!')
    green.value(0)
    yellow.value(1)
    red.value(0)
    time.sleep(2)

    # RED - 5 seconds
    print('RED - Ruko!')
    green.value(0)
    yellow.value(0)
    red.value(1)
    time.sleep(5)
