from gpiozero import PWMOutputDevice


class Led(PWMOutputDevice):

    name: str = ""

    def _write(self, value):
        super(Led, self)._write(1 - value)

    def on(self):
        self._write(True)

    def off(self):
        self._write(False)
