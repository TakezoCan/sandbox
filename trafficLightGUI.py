#!/usr/bin/env python3

#
# Filename: trafficLightGUI.py
# Date: 2018.10.31
# Author: Curtis Girling
# Function: Runs three LEDs as a traffic light with GUI interface
#

from guizero import App, PushButton, Text  # GUI interface app
from time import sleep # import sleep function for delay timing
import RPi.GPIO as GPIO # import GPIO library to use GPIO pins

# Lables for BCM pin numbers
greenLed = 18
yellowLed = 22
redLed = 25
state = False

#pushNum = 4

GPIO.setwarnings(False) # stop warnings from displaying
GPIO.setmode(GPIO.BCM) # BCM numbering scheme for breakout board
GPIO.setup(greenLed,GPIO.OUT) # sets variable greenLed to an output
GPIO.setup(yellowLed,GPIO.OUT) # sets variable yellowLed to an output
GPIO.setup(redLed,GPIO.OUT) # sets variable redLed to an output
#GPIO.setup(pushNum,GPIO.IN, pull_up_down=GPIO.PUD_UP) # sets variable pushNum to an input

def counter():
    text.value = int(text.value) + 1

def pause():
    sleep(3.0)
    
def delay_green(): # Turns on BCM output 18
    print("Green ON")
    GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
    GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
    GPIO.output(greenLed,GPIO.HIGH) # Turns on greenLed

def delay_yellow(): # Turns on BCM output 22
    print("Yellow ON")
    GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
    GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
    GPIO.output(yellowLed,GPIO.HIGH)# Turns on yellowLed

def delay_red(): # Turns on BCM output 25
    print("Red ON")
    GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
    GPIO.output(greenLed,GPIO.LOW)  # Turns off greenLed
    GPIO.output(redLed,GPIO.HIGH)   # Turns on redLed
    
    
def run_green(): 
    app.after(3000, delay_green) # 3 second delay before running script
    
def run_yellow(): 
    app.after(6000, delay_yellow) # 3 second delay before running script
    
def run_red():  
    app.after(9000, delay_red)  # 3 second delay before running script 


def run_cleanUP():
    GPIO.output(redLed,GPIO.LOW)    # Turns off redLed
    GPIO.output(yellowLed,GPIO.LOW) # Turns off yellowLed
    GPIO.output(greenLed,GPIO.LOW) # Turns off greenLed

def start():
    start_button.disable()
    stop_button.enable()
    message.value = "Traffic lights ON" # Displays message in GUI
    print("Traffic lights ON")
    app.repeat(100,run_green) # Repeat run_lights loop)
    app.repeat(100,run_yellow) # Repeat run_yellow loop
    app.repeat(100,run_red) # Repeat run_red loop




def stop():
    start_button.enable()
    stop_button.disable()
    app.cancel(run_green) # Cancels run_lights loop
    app.cancel(run_yellow) # Cancels run_yellow loop
    app.cancel(run_red) # Cancels run_red loop
    #GPIO.cleanup() # Clean up GPIO pins
    run_cleanUP()
    message.value = "Traffic lights OFF"
    #message.color = "red"
    print("Traffic lights OFF")

#Start of GUI Loop
app = App(title="Trafic Lights",width=300, height=200, layout="auto") # Sets up GUI window

print("Traffic lights OFF")
message = Text(app, text="Traffic lights OFF", size=20, font="Times New Roman", color="Black")

start_button = PushButton(app, command=start, text="START")
stop_button = PushButton(app, command=stop, text="STOP", enabled=False)
start_button.bg="lightgreen"
stop_button.bg="pink"

text = Text(app, text="1")
text.repeat(1000, counter)  # Schedule call to counter() every 1000ms


app.display() # Similar to While loop. Runs from "app=..." to "app.display"
#End of GUI loop
