import time

from Pyled import LEDs

try:
    while True:
        for led in LEDs:
            print(led.name + ": on")
            led.on()
            time.sleep(1)
            print(led.name + ": off")
            led.off()
            time.sleep(1)

except KeyboardInterrupt:
    for led in LEDs:
        led.close()
    exit(0)
