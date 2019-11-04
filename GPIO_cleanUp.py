#!/usr/bin/env python3

#
# Filename: GPIO_cleanUp.py
# Date: 2018.10.31
# Author: Curtis Girling
# Function: Runs three LEDs as a traffic light when button is pressed
#

from time import sleep 
import RPi.GPIO as GPIO # import GPIO library to use GPIO pins


GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BCM) # BCM numbering scheme for breakout board
GPIO.setup(18,GPIO.OUT) # sets variable pin 18 to an output
GPIO.setup(22,GPIO.OUT) # sets variable pin 22 to an output
GPIO.setup(25,GPIO.OUT) # sets variable pin 15 to an output


GPIO.output(18,GPIO.LOW) # Turns off pin 18
GPIO.output(22,GPIO.LOW) # Turns off pin 22
GPIO.output(25,GPIO.LOW) # Turns off pin 25

    

sleep(0.1) #Wait 0.1 seconds

print("outputs 18, 22, 25 OFF")


GPIO.cleanup() # Clean up GPIO pins