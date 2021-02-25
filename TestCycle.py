from gpiozero import LED
from time import sleep

red = LED(2)
green = LED(3)
blue = LED(4)
LEDs = [red, green, blue]

enable: bool = True
try:
    while True:
        for LED in LEDs:
            if enable:
                LED.on()
            else:
                LED.off()
            sleep(1)

        enable = not enable
        print("Looping...")

except KeyboardInterrupt:
    red.close()
    blue.close()
    green.close()
