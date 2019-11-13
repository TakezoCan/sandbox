#!/usr/bin/env python3

#
# Filename: GPIO_BCM25.py
# Date: 2018.11.13
# Author: Curtis Girling
# Function: turns on BCM output 25
#

import RPi.GPIO as GPIO # import GPIO library to use GPIO pins


GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BCM) # BCM numbering scheme for breakout board
GPIO.setup(25,GPIO.OUT) # sets variable pin 15 to an output


GPIO.output(25,GPIO.HIGH) # Turns off pin 25


print("outputs 25 ON")

