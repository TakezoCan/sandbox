#!/usr/bin/env python3

#
# Filename: senseHat_test.py
# Date: 2018.11.01
# Author: Curtis Girling
# Function: practice program, Sense Hat animatiom
#


from time import sleep # import sleep function for delay timing
from sense_hat import SenseHat


sense = SenseHat()

w = (150, 150, 150)
b = (0, 0, 255)
e = (0, 0, 0)

image = [
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
w,w,w,e,e,w,w,w,
w,w,b,e,e,w,w,b,
w,w,w,e,e,w,w,w,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e,
e,e,e,e,e,e,e,e
]

try:
    sense.set_pixels(image)
    while True:
        sleep(1) #Wait 1 seconds
        sense.flip_h()   

        
finally: # This block will run no matter how the try block exits
  sense.clear()