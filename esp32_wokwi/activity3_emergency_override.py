# Activity 3 - Emergency Override (ambulance button)
# Circuit: same 3 LEDs as Activity 2 + pushbutton between GPIO 15 and GND
from machine import Pin
import time

green = Pin(4, Pin.OUT)
yellow = Pin(5, Pin.OUT)
red = Pin(2, Pin.OUT)
emergency = Pin(15, Pin.IN, Pin.PULL_UP)   # pressed = 0 (because of pull-up)


def all_off():
    green.value(0)
    yellow.value(0)
    red.value(0)


def emergency_green():
    print('EMERGENCY! Ambulance detected - GREEN override!')
    all_off()
    green.value(1)
    time.sleep(5)          # 5 seconds green for the ambulance
    all_off()


all_off()
print('Traffic Light ready! Button = Emergency override')

while True:
    # Emergency check pehle
    if emergency.value() == 0:
        emergency_green()
        continue

    # Normal GREEN (check button every 0.1 s)
    print('GREEN - Normal cycle')
    all_off()
    green.value(1)
    for _ in range(50):
        if emergency.value() == 0:
            emergency_green()
            break
        time.sleep(0.1)

    # Normal YELLOW
    print('YELLOW - Slow down')
    all_off()
    yellow.value(1)
    time.sleep(2)

    # Normal RED (check button every 0.1 s)
    print('RED - Stop')
    all_off()
    red.value(1)
    for _ in range(50):
        if emergency.value() == 0:
            emergency_green()
            break
        time.sleep(0.1)
