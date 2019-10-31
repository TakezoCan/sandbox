#!/usr/bin/env python3

#
# Filename: trafficLight.py
# Date: 2018.10.31
# Author: Curtis Girling
# Function: Runs three LEDs as a traffic light when button is pressed
#

from guizero import App, PushButton, Text # GUI interface app
from time import sleep # import sleep function for delay timing
import RPi.GPIO as GPIO # import GPIO library to use GPIO pins

# Lables for BCM pin numbers
greenLed = 18
yellowLed = 22
redLed = 25
#state = False

#pushNum = 4

GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BCM) # BCM numbering scheme for breakout board
GPIO.setup(greenLed,GPIO.OUT) # sets variable greenLed to an output
GPIO.setup(yellowLed,GPIO.OUT) # sets variable yellowLed to an output
GPIO.setup(redLed,GPIO.OUT) # sets variable redLed to an output
#GPIO.setup(pushNum,GPIO.IN, pull_up_down=GPIO.PUD_UP) # sets variable pushNum to an input


def turn_on():
    state.value = True

    #message = Text(app, text="Traffic lights ON", size=20, font="Times New Roman", color="green", grid=[0,0], align="left")
    #try:

     #   while True: # This will continue to run until you press Ctrl-C
     #       GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
     #       GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
     #       GPIO.output(greenLed,GPIO.HIGH) # Turns on greenLed
     #       sleep(3.0)  # Wait 3 seconds

     #       GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
     #       GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
     #       GPIO.output(yellowLed,GPIO.HIGH)# Turns on yellowLed
     #       sleep(3.0)  # Wait 3 seconds

     #       GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
     #       GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
     #       GPIO.output(redLed,GPIO.HIGH)   # Turns on redLed
     #       sleep(3.0)  # Wait 3 seconds



    #finally: # This block will run no matter how the try block exits
    #  GPIO.cleanup() # Clean up GPIO pins



app = App(title="Traffic Lights", width=300, height=200, layout="grid")
print("Lights OFF")
state = False
message = Text(app, text="Traffic lights Off", size=20, font="Times New Roman", color="red", grid=[0,0], align="left")

change_state = PushButton(app, command=turn_on, text="Run Lights", grid=[1,3], align="left")
#sleep(0.1)

if (state == True):
    #message = Text(app, text="Traffic lights ON", size=20, font="Times New Roman", color="green", grid=[0,0], align="left")
    try:
        print("Lights ON")
        while True:
            GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
            GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
            GPIO.output(greenLed,GPIO.HIGH) # Turns on greenLed
            sleep(3.0)  # Wait 3 seconds

            GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
            GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
            GPIO.output(yellowLed,GPIO.HIGH)# Turns on yellowLed
            sleep(3.0)  # Wait 3 seconds

            GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
            GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
            GPIO.output(redLed,GPIO.HIGH)   # Turns on redLed
            sleep(3.0)  # Wait 3 seconds
    finally: # This block will run no matter how the try block exits
        GPIO.cleanup() # Clean up GPIO pins


app.display()
