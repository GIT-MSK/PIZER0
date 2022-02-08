#!/usr/bin/env python3

NULL_CHAR = chr(0)

def write_report(report):
    with open('/dev/hidg0', 'rb+') as fd:
        fd.write(report.encode())

# Adding proper values to keychars
def chrParser(num):
    return NULL_CHAR*2+chr(num)+NULL_CHAR*5

# Keyboard chars
# a = 0x04
# b = 0x05
# c = 0x06
# d = 0x07
# e = 0x08
# f = 0x09
# g = 0x0a
# h = 0x0b
# i = 0x0c
# j = 0x0d
# k = 0x0e
# l = 0x0f
# m = 0x10
# n = 0x11
# o = 0x12
# p = 0x13
# q = 0x14
# r = 0x15
# s = 0x16
# t = 0x17
# u = 0x18
# v = 0x19
# w = 0x1a
# x = 0x1b
# y = 0x1c
# z = 0x1d
# enter = 40
# space = 44
# release = NULL_CHAR*8
# shift = chr(32)

charList = {
    'a': 0x04,
    'b': 0x05,
    'c': 0x06,
    'd': 0x07,
    'e': 0x08,
    'f': 0x09,
    'g': 0x0a,
    'h': 0x0b,
    'i': 0x0c,
    'j': 0x0d,
    'k': 0x0e,
    'l': 0x0f,
    'm': 0x10,
    'n': 0x11,
    'o': 0x12,
    'p': 0x13,
    'q': 0x14,
    'r': 0x15,
    's': 0x16,
    't': 0x17,
    'u': 0x18,
    'v': 0x19,
    'w': 0x1a,
    'x': 0x1b,
    'y': 0x1c,
    'z': 0x1d,
}

for x, y in charList.items():
    print(x, y)


# write_report(chrParser(0x04))

# Modifiers
# enter = NULL_CHAR*2+chr(40)+NULL_CHAR*5

# space = NULL_CHAR*2+chr(44)+NULL_CHAR*5
# shift = chr(32)

# for i in range(50):
#     write_report(chrParser())

# Release all keys
write_report(NULL_CHAR*8)
#Press a
# write_report(NULL_CHAR*2+chr(4)+NULL_CHAR*5)
# # Release keys
# write_report(NULL_CHAR*8)
# # Press SHIFT + a = A
# write_report(chr(32)+NULL_CHAR+chr(4)+NULL_CHAR*5)

# # Press b
# write_report(NULL_CHAR*2+chr(5)+NULL_CHAR*5)
# # Release keys
# write_report(NULL_CHAR*8)
# # Press SHIFT + b = B
# write_report(chr(32)+NULL_CHAR+chr(5)+NULL_CHAR*5)

# # Press SPACE key
# write_report(NULL_CHAR*2+chr(44)+NULL_CHAR*5)

# # Press c key
# write_report(NULL_CHAR*2+chr(6)+NULL_CHAR*5)
# # Press d key
# write_report(NULL_CHAR*2+chr(7)+NULL_CHAR*5)

# # Press RETURN/ENTER key
# write_report(NULL_CHAR*2+chr(40)+NULL_CHAR*5)

# # Press e key
# write_report(NULL_CHAR*2+chr(8)+NULL_CHAR*5)
# # Press f key
# write_report(NULL_CHAR*2+chr(9)+NULL_CHAR*5)


