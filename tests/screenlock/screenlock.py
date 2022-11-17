import Adafruit_BBIO.GPIO as GPIO
import os
import time, threading

class ScreenLock:
    def __init__(self, gpio_pin = 'P9_17'):
        GPIO.setup(gpio_pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        t = threading.Thread(target = self._click)
        t.start()

    def powerOff():
        """ Disable GPIOs here
        """

    def powerOn():
        """ Enable GPIOs here
        """

    def _click(self):
        lock = False
        while True:
            GPIO.wait_for_edge("P9_17", GPIO.FALLING)
            if lock == False:
                os.system('xset -display :0.0 s noblank')
                os.system('xset -display :0.0 s activate')
            else:
                os.system('xset -display :0.0 dpms force on')

            lock = not lock
