from gpiozero import LED

class TrafficLights:
    def __init__(self, red_pin, yellow_pin, green_pin):
        self.red = LED(red_pin)
        self.yellow = LED(yellow_pin)
        self.green = LED(green_pin)

    def _all_off(self):
        self.red.off()
        self.yellow.off()
        self.green.off()

    def red_on(self):
        self._all_off()
        self.red.on()

    def yellow_on(self):
        self._all_off()
        self.yellow.on()

    def green_on(self):
        self._all_off()
        self.green.on()
