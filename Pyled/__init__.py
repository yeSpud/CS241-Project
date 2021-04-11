from typing import List

from .gpio_led import Led

red: Led = Led(2)
red.name = "Red"

green: Led = Led(3)
green.name = "Green"

blue: Led = Led(4)
blue.name = "Blue"

LEDs: List[Led] = [red, green, blue]
