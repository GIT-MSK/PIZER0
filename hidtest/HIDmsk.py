
from hidtest.keycode import NULL_CHAR, charList, modifierList
import sys
import os

# sys.path.insert(0,'<project directory>') OR
# sys.path.append(os.getcwd())

# keyboard device handling


def sendChar(char):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(char.encode())

# ---------------------------------------------------- Translation functions

# Adding machine-readable values to keychars


def charParser(num):
    return NULL_CHAR*2+chr(num)+NULL_CHAR*5

# Modifiers takes up the first of the 8-byte segment


def modifierParser(mod):
    return chr(mod)+NULL_CHAR*7

# Pressing a modifier the same time as a regular key, example GUI + R


def press2gether(mod, key):
    return chr(mod)+NULL_CHAR+chr(key)+NULL_CHAR*5

# Sends NULL to all eight bytes


def releaseKeys():
    return sendChar(NULL_CHAR*8)

# ---------------------------------------------------- output functions

# Sending output to target


def outputChar(value):
    sendChar(charParser(charList[value]))
    releaseKeys()

# Sending a modifier value to target


def outputMod(value):
    sendChar(modifierParser(modifierList[value]))
    releaseKeys()

# For sending a modifier + key


def outputHoldMod(mod, key):
    sendChar(press2gether(modifierList[mod], charList[key]))
    releaseKeys()


# ---------------------------------------------------- functions

def writeString(string):
    for k in string:
        try:
            k = k.upper()

            # Find a better way to do this for all keys with corresponding keycodes
            if (k == " "):
                k = "SPACE"
            if (k == "\n"):
                k = "ENTER"
            if(k == ","):
                k = "COMMA"
            if(k == "."):
                k = "DOT"
            if(k == "/"):
                k = "SLASH"
            if(k == ":"):
                outputHoldMod("SHIFT", "SEMICOLON")
                continue
            if(k == "!"):
                outputHoldMod("SHIFT", "1")
                continue
            # print(str(k))
            outputChar(f"{k}")
            # print(str(k))
            # releaseKeys()

        except:
            print(f"Unknown char {k}")
            releaseKeys()


print("Done Writing.")


# Release all keys
sendChar(NULL_CHAR*8)
