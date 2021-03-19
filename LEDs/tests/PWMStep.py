from gpiozero import PWMLED
import time

led = PWMLED(3)
led.on()

time.sleep(1)

try:
    for i in range(0, 4):
        val = 1 / (i + 1)
        print("Pwm: " + str(val))
        led.value = val
        time.sleep(0.5)

    led.value = 0
    time.sleep(1)
except KeyboardInterrupt:
    led.close()
    exit(0)
