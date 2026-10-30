# Activity 4 - Dual Lane Competition: busiest lane wins the green light
# Circuit: GPIO 4 North green, GPIO 2 North red, GPIO 18 South green,
#          GPIO 19 South red (LEDs via 220 ohm), GPIO 15 / GPIO 16 buttons to GND
from machine import Pin
import time

# Lane 1 (North)
north_green = Pin(4, Pin.OUT)
north_red = Pin(2, Pin.OUT)
btn_north = Pin(15, Pin.IN, Pin.PULL_UP)

# Lane 2 (South)
south_green = Pin(18, Pin.OUT)
south_red = Pin(19, Pin.OUT)
btn_south = Pin(16, Pin.IN, Pin.PULL_UP)

north_count = 0
south_count = 0


def set_signals(north_wins):
    if north_wins:
        north_green.value(1); north_red.value(0)
        south_green.value(0); south_red.value(1)
        print(f'NORTH GREEN! ({north_count} vehicles)')
    else:
        north_green.value(0); north_red.value(1)
        south_green.value(1); south_red.value(0)
        print(f'SOUTH GREEN! ({south_count} vehicles)')


print('Competition start! 10 seconds mein zyada button dabao!')
print('Button A = North lane | Button B = South lane')

while True:
    north_count = 0
    south_count = 0
    print('--- New Round --- 10 seconds!')

    # 10 second counting window
    start = time.time()
    while time.time() - start < 10:
        if btn_north.value() == 0:
            north_count += 1
            print(f'North: {north_count}')
            time.sleep(0.2)          # debounce
        if btn_south.value() == 0:
            south_count += 1
            print(f'South: {south_count}')
            time.sleep(0.2)          # debounce

    # Winner
    print(f'Result - North: {north_count} | South: {south_count}')
    set_signals(north_count >= south_count)
    time.sleep(5)                    # 5 s green, then a new round
