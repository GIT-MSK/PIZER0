# PIZERO

## Purpose

Projects made to see what is possible with the RPi Zero 2W

## Temp

HID device

## Documentation

Start every payload by importing the main HID file

example:

```py

from HIDmsk import *

```

You can write advanced HID scripts using the functions decalred here:

```py

# Sends a single char to the target
def outputChar(char)

# Sending a modifier value to target, think WINDOWS button
def outputMod(value):

# For sending a modifier + key
def outputHoldMod(mod, key):

# Sends an entire string, funky with special chars, use the outputChar() function for those
def writeString(string)

```

# Todo
 - More GUI Keys
 - Find a better way of handling the unknown keys
 - Make the device be able to read strings from files
