import time
from signal import pause

from gpiozero import PWMLED

red = PWMLED(2)
green = PWMLED(3)
blue = PWMLED(4)

try:
    red.pulse()
    time.sleep(1)
    green.pulse()
    time.sleep(0.5)
    blue.pulse(fade_out_time=0.5)

    pause()

except KeyboardInterrupt:
    red.close()
    green.close()
    blue.close()
    exit(0)
