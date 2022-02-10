# PIZERO

## Purpose

Projects currently in development to see what is possible with the RPI Zero 2 W.

## Hardware used in this project:

Raspberry Pi: [Pi Zero 2 W ](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)  
Screen: [Adafruit 1.3" TFT color bonnet ](https://learn.adafruit.com/adafruit-1-3-color-tft-bonnet-for-raspberry-pi)

## Installation

Setting up the PI as an [HID device](https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition/)
[Screen Drivers](https://learn.adafruit.com/adafruit-1-3-color-tft-bonnet-for-raspberry-pi/python-setup)  

## Documentation

### BADUSB with the ability to use advanced python scripting and modules

Start every payload by importing the main HID file

example:

```py

from HIDmsk import *

```

You can write advanced HID scripts using the functions decalred here:

```py

# Sends a single char to the target
def outputChar(char):

# Sending a modifier value to target, think WINDOWS button
def outputMod(value):

# For sending a modifier + key
def outputHoldMod(mod, key):

# Sends an entire string, funky with special chars, use the outputChar() function for those
def writeString(string):


```

#### Example hello world program

```py

from HIDmsk import *


def main():
    outputHoldMod('KEY_GUI', 'KEY_R')

    time.sleep(1)

    writeString("notepad.exe")

    time.sleep(1)

    outputChar("KEY_ENTER")

    time.sleep(1)

    writeString("Hello From RP Zero 2 W!")


main()


```

# Todo
 - More GUI Keys
 - Find a better way of handling the unknown keys
 - Make the device be able to read strings from files
