#!/usr/bin/python2

import RPi.GPIO as GPIO
import time
import subprocess

class Button(object):
    def __init__(self, pin):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(pin, GPIO.IN)

        self.pressedAt = 0

        GPIO.add_event_detect(pin, GPIO.BOTH, callback=self.btnCB, bouncetime=300)

    def pressed(self):
        self.pressedAt = time.time()

    def released(self):
        if (self.pressedAt and (time.time()-self.pressedAt > 3)):
            subprocess.call(['poweroff'])
        self.pressedAt = 0

    def btnCB(self, channel):
        time.sleep(.5)
        if GPIO.input(channel):
            self.released()
        else:
            self.pressed()

try:
    button = Button(pin=8)

    while True:
        time.sleep(9999)
except:
    GPIO.cleanup()
