import time

from LEDs.src import LEDs

time.sleep(1)

try:
    for led in LEDs:
        for i in range(0, 4):
            val = 1 / (i + 1)
            print(led.name + ": " + str(val))
            led.value = val
            time.sleep(0.75)

        led.value = 0
        time.sleep(1)
except KeyboardInterrupt:
    for led in LEDs:
        led.close()
    exit(0)
