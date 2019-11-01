#!/usr/bin/env python3

#
# Filename: trafficLightGUI.py
# Date: 2018.10.31
# Author: Curtis Girling
# Function: Runs three LEDs as a traffic light with GUI interface
#

from guizero import App, PushButton, Text  # GUI interface app
from time import sleep # import sleep function for delay timing
#import RPi.GPIO as GPIO # import GPIO library to use GPIO pins

# Lables for BCM pin numbers
#greenLed = 18
#yellowLed = 22
#redLed = 25
#state = False

#pushNum = 4

#GPIO.setwarnings(False) # stop warnings from displaying
#GPIO.setmode(GPIO.BCM) # BCM numbering scheme for breakout board
#GPIO.setup(greenLed,GPIO.OUT) # sets variable greenLed to an output
#GPIO.setup(yellowLed,GPIO.OUT) # sets variable yellowLed to an output
#GPIO.setup(redLed,GPIO.OUT) # sets variable redLed to an output
#GPIO.setup(pushNum,GPIO.IN, pull_up_down=GPIO.PUD_UP) # sets variable pushNum to an input

def counter():
    text.value = int(text.value) + 1

def run_lights(): #opperates outputs
    #if (start_button.enable == False):
    print("Running Lights")
    #GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
    #GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
    #GPIO.output(greenLed,GPIO.HIGH) # Turns on greenLed
    #sleep(3.0)  # Wait 3 seconds

    #GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
    #GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
    #GPIO.output(yellowLed,GPIO.HIGH)# Turns on yellowLed
    #sleep(3.0)  # Wait 3 seconds

    #GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
    #GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
    #GPIO.output(redLed,GPIO.HIGH)   # Turns on redLed
    #sleep(3.0)  # Wait 3 seconds


def start():
    start_button.disable()
    stop_button.enable()
    start_button.repeat(100,run_lights)
    message.value = "Traffic lights ON"
    #message.color = "green"
    print("Traffic lights ON")


def stop():
    start_button.enable()
    stop_button.disable()
    stop_button.cancel(run_lights)
    #GPIO.cleanup() # Clean up GPIO pins
    message.value = "Traffic lights OFF"
    #message.color = "red"
    print("Traffic lights OFF")

app = App(title="Trafic Lights",width=300, height=200, layout="auto")

print("Traffic lights OFF")
message = Text(app, text="Traffic lights OFF", size=20, font="Times New Roman", color="Black")

start_button = PushButton(app, command=start, text="START")
stop_button = PushButton(app, command=stop, text="STOP", enabled=False)
start_button.bg="lightgreen"
stop_button.bg="pink"

text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms


app.display()


