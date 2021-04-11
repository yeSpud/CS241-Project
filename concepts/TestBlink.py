from gpiozero import LED

red = LED(2)
green = LED(3)
blue = LED(4)
LEDs = [red, green, blue]

green.blink(on_time=1, off_time=1, n=5, background=False)
green.blink(on_time=0.5, off_time=0.5, n=5, background=False)
green.blink(on_time=0.25, off_time=0.25, n=5, background=False)
green.blink(on_time=0.1, off_time=0.1, n=5, background=False)
