# ESP32 + MicroPython (Wokwi) Activities

Hardware-bridge activities done **before the real Jetson Nano hardware**, using the free
[Wokwi](https://wokwi.com/projects/new/micropython-esp32) simulator (ESP32-S3, MicroPython).
Full explanations are in [`docs/ESP32_MicroPython_Activities.pdf`](../docs/ESP32_MicroPython_Activities.pdf).

| File | Activity | Pins |
|---|---|---|
| `activity1_led_blink.py` | Blink one LED | GPIO 2 |
| `activity2_traffic_light.py` | Red / Yellow / Green cycle | GPIO 2 (R), 5 (Y), 4 (G) |
| `activity3_emergency_override.py` | Button = ambulance, forces green | + GPIO 15 button |
| `activity4_dual_lane.py` | Two lanes compete, busiest gets green | GPIO 4/2, 18/19, buttons 15/16 |

## How to run
1. Open Wokwi → **New Project → MicroPython on ESP32**.
2. Build the circuit shown in the PDF (LEDs with 220 Ω resistors, pushbuttons to GND).
3. Paste a file's code into `main.py` (not `sketch.ino`) and press **Play**.

> The idea: button press = "YOLO detected a vehicle", so Activity 4 is the same logic the
> final system uses to give green to the lane with the most detected vehicles.
