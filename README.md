# PIZer0

## Prototype

![Prototype](img/20220217_233918.jpg)

## Purpose

The project currently not being developed. Might continue sometime in the future.

NB! This is a work in progress, none of the code is final, contains bugs and takes inspiration from other projects.

Everything created is created for my own educational purposes.

## Hardware used in this project:

Raspberry Pi: [Pi Zero 2 W ](https://www.raspberrypi.com/products/raspberry-pi-zero-2-w/)  
Screen: [Adafruit 1.3" TFT color bonnet ](https://learn.adafruit.com/adafruit-1-3-color-tft-bonnet-for-raspberry-pi)

## Installation

Setting up the PI as an [HID device](https://www.rmedgar.com/blog/using-rpi-zero-as-keyboard-setup-and-device-definition/)  
[Screen Drivers](https://learn.adafruit.com/adafruit-1-3-color-tft-bonnet-for-raspberry-pi/python-setup) and setup

If you have the same display, run the display.py file to show the GUI after everything is set up.

## Documentation

### BadUSB with the ability to use advanced python scripting and modules

> NB! The USB-cable or USB-addon has to be connected to the data-port on the RPIzero

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
    outputHoldMod('GUI', 'R')

    time.sleep(1)

    writeString("notepad.exe")

    time.sleep(1)

    outputChar("ENTER")

    time.sleep(2)

    for i in range(5):
        writeString("Hello From RPI Zero 2 W!\n")

if __name__ == '__main__':
    main()

```

# Todo
 - Find a better way of handling the unknown keys
 - Make the device be able to read strings from files
 - Make a function to treat the modifier bit the same way as a normal report?
 - Make the HIDmsk file act as a module so it can be placed anywhere
 - Find a cleaner way of handling button presses
 - Make the payloads menu indexable and scrollable
