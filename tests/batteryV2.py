import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.ADC as ADC
import time

class BatteryV2:
    voltage_level = [1.4, 1.48, 1.58, 1.68]
    level = "power100"
    def isCharge(self):
        return GPIO.input(self.charge)

    def __init__(self, charge, adc, _callback):
        # Instance Variables
        self.charge = charge
        self.adc = adc
        self.callback = _callback

    def setUp(self):
        # GPIO
        # https://adafruit-beaglebone-io-python.readthedocs.io/en/latest/GPIO.html
        GPIO.setup(self.charge, GPIO.IN, GPIO.PUD_UP)
        GPIO.add_event_detect(self.charge, GPIO.FALLING)
        GPIO.add_event_callback(self.charge, callback=self.callback)
        
        # ADC
        # https://adafruit-beaglebone-io-python.readthedocs.io/en/latest/ADC.html
        ADC.setup()

    def voltage(self):
        return ADC.read(self.adc) * 1.8

    def batteryLevel(self, voltage):
        if voltage > self.voltage_level[-1]:
            return "power100"
        if voltage <= self.voltage_level[0]:
            return "power0"
        if voltage > self.voltage_level[2]:
            return "power75"
        if voltage > self.voltage_level[1]:
            return "power50"
        if voltage > self.voltage_level[0]:
            return "power25"

def charge_callback(channel):
    print("callback called for " + channel)
