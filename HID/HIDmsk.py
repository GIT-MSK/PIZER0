#!/usr/bin/env python3

import time

NULL_CHAR = chr(0)

# Chars modified from https://github.com/ddavid456/NetworkPiKeyboard/blob/master/NetworkKeyboardAPI.py
# Modifiers from https://gist.github.com/MightyPork/6da26e382a7ad91b5496ee55fdc73db2
# Corresponds with US ANSI

charList = {
    'A': 0x04, 'B': 0x05,
    'C': 0x06, 'D': 0x07,
    'E': 0x08, 'F': 0x09,
    'G': 0x0a, 'H': 0x0b,
    'I': 0x0c, 'J': 0x0d,
    'K': 0x0e, 'L': 0x0f,
    'M': 0x10, 'N': 0x11,
    'O': 0x12, 'P': 0x13,
    'Q': 0x14, 'R': 0x15,
    'S': 0x16, 'T': 0x17,
    'U': 0x18, 'V': 0x19,
    'W': 0x1a, 'X': 0x1b,
    'Y': 0x1c, 'Z': 0x1d,
    '1': 0x1e, '2': 0x1f,
    '3': 0x20, '4': 0x21,
    '5': 0x22, '6': 0x23,
    '7': 0x24, '8': 0x25,
    '9': 0x26, '0': 0x27,
    'ENTER': 0x28, 'ESC': 0x29,
    'BACKSPACE': 0x2a, 'TAB': 0x2b,
    'SPACE': 0x2c, 'MINUS': 0x2d,
    'EQUAL': 0x2e, 'LEFTBRACE': 0x2f,
    'RIGHTBRACE': 0x30, 'BACKSLASH': 0x31,
    'HASHTILDE': 0x32, 'SEMICOLON': 0x33,
    'APOSTROPHE': 0x34, 'GRAVE': 0x35,
    'COMMA': 0x36, 'DOT': 0x37,
    'SLASH': 0x38, 'CAPSLOCK': 0x39,
    'F1': 0x3a, 'F2': 0x3b,
    'F3': 0x3c, 'F4': 0x3d,
    'F5': 0x3e, 'F6': 0x3f,
    'F7': 0x40, 'F8': 0x41,
    'F9': 0x42, 'F10': 0x43,
    'F11': 0x44, 'F12': 0x45,
    'F13': 0x68, 'F14': 0x69,
    'F15': 0x6a, 'F16': 0x6b,
    'F17': 0x6c, 'F18': 0x6d,
    'F19': 0x6e, 'F20': 0x6f,
    'F21': 0x70, 'F22': 0x71,
    'F23': 0x72, 'F24': 0x73,
    'SYSRQ': 0x46, 'SCROLLLOCK': 0x47,
    'PAUSE': 0x48, 'INSERT': 0x49,
    'HOME': 0x4a, 'PAGEUP': 0x4b,
    'DELETE': 0x4c, 'END': 0x4d,
    'PAGEDOWN': 0x4e, 'RIGHT': 0x4f,
    'LEFT': 0x50, 'DOWN': 0x51,
    'UP': 0x52, 'MEDIA_PLAYPAUSE': 0xe8,
    'MEDIA_STOPCD': 0xe9, 'MEDIA_PREVIOUSSONG': 0xea,
    'MEDIA_NEXTSONG': 0xeb, 'MEDIA_EJECTCD': 0xec,
    'MEDIA_VOLUMEUP': 0xed, 'MEDIA_VOLUMEDOWN': 0xee,
    'MEDIA_MUTE': 0xef, 'MEDIA_WWW': 0xf0,
    'MEDIA_BACK': 0xf1, 'MEDIA_FORWARD': 0xf2,
    'MEDIA_STOP': 0xf3, 'MEDIA_FIND': 0xf4,
    'MEDIA_SCROLLUP': 0xf5, 'MEDIA_SCROLLDOWN': 0xf6,
    'MEDIA_EDIT': 0xf7, 'MEDIA_SLEEP': 0xf8,
    'MEDIA_COFFEE': 0xf9, 'MEDIA_REFRESH': 0xfa,
    'MEDIA_CALC': 0xfb, 'OPEN': 0x74,
    'HELP': 0x75, 'PROPS': 0x76,
    'FRONT': 0x77, 'STOP': 0x78,
    'AGAIN': 0x79, 'UNDO': 0x7a,
    'CUT': 0x7b, 'COPY': 0x7c,
    'PASTE': 0x7d, 'FIND': 0x7e,
    'MUTE': 0x7f, 'VOLUMEUP': 0x80,
    'VOLUMEDOWN': 0x81,
}

modifierList = {
    'CTRL': 0x01,
    'SHIFT': 0x02,
    'ALT': 0x04,
    'GUI': 0x08,
    'RCTRL': 0x10,
    'RSHIFT': 0x20,
    'RALT': 0x40,
    'RGUI': 0x80,
}


# ---------------------------------------------------- Translation functions

# keyboard device handling


def sendChar(char):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(char.encode())

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
