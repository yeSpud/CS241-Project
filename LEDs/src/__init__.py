from typing import List

from gpio_led import Led

red: Led = Led(2)
red.__name__ = "Red"

green: Led = Led(3)
green.__name__ = "Green"

blue: Led = Led(4)
blue.__name__ = "Blue"

LEDs: List[Led] = [red, green, blue]
