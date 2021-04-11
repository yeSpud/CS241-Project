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
                print("On")
                LED.on()
            else:
                print("Off")
                LED.off()
            sleep(1)

        enable = not enable

except KeyboardInterrupt:
    red.close()
    blue.close()
    green.close()
