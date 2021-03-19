from LEDs.src import *
import time

try:
    while True:
        for led in LEDs:
            print(led.__name__ + ": on")
            led.on()
            time.sleep(1)
            print(led.__name__ + ": off")
            led.off()
            time.sleep(1)

except KeyboardInterrupt:
    for led in LEDs:
        led.close()
    exit(0)
