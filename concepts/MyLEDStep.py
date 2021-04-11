import time

from Pyled import LEDs

time.sleep(1)

m = 20

try:
    for led in LEDs:
        for index in range(0, m+1):
            v = index / m
            print(led.name + ": " + str(v))
            led.value = v
            time.sleep(0.75)

        led.value = 0
        time.sleep(1)
except KeyboardInterrupt:
    for led in LEDs:
        led.close()
    exit(0)
