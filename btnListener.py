#!/usr/bin/python2

import RPi.GPIO as GPIO
import time, subprocess

def pressed():
    global pressedAt
    pressedAt = time.time()

def released():
    global pressedAt
    if (pressedAt and (time.time()-pressedAt > 3)):
        subprocess.call(['poweroff'])
        pressedAt = 0    # Not necessary, but doesn't hurt
    else:
        pressedAt = 0

def btnCB(channel):
    time.sleep(.5)
    if GPIO.input(channel):
        released()
    else:
        pressed()

try:
    GPIO.setwarnings(False) 
    btnPin = 8
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(btnPin, GPIO.IN)

    pressedAt = 0

    GPIO.add_event_detect(btnPin, GPIO.BOTH, callback=btnCB, bouncetime=300)

    while True:
        time.sleep(9999)
except:
    GPIO.cleanup()

