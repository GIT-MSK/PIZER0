# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

# -*- coding: utf-8 -*-

from hashlib import new
import time
import subprocess
from digitalio import DigitalInOut, Direction
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789


# Configuration for CS and DC pins (these are FeatherWing defaults on M0/M4):
cs_pin = DigitalInOut(board.CE0)
dc_pin = DigitalInOut(board.D25)
reset_pin = DigitalInOut(board.D24)

# Config for display baudrate (default max is 24mhz):
BAUDRATE = 64000000

# Setup SPI bus using hardware SPI:
spi = board.SPI()

# Create the ST7789 display:
disp = st7789.ST7789(
    spi,
    cs=cs_pin,
    dc=dc_pin,
    rst=reset_pin,
    baudrate=BAUDRATE,
    width=240,
    height=240,
    x_offset=0,
    y_offset=80,
)

# Turn on the backlight
backlight = DigitalInOut(board.D26)
backlight.switch_to_output()
backlight.value = True

# Input pins:
button_A = DigitalInOut(board.D5)
button_A.direction = Direction.INPUT

button_B = DigitalInOut(board.D6)
button_B.direction = Direction.INPUT

button_L = DigitalInOut(board.D27)
button_L.direction = Direction.INPUT

button_R = DigitalInOut(board.D23)
button_R.direction = Direction.INPUT

button_U = DigitalInOut(board.D17)
button_U.direction = Direction.INPUT

button_D = DigitalInOut(board.D22)
button_D.direction = Direction.INPUT

button_C = DigitalInOut(board.D4)
button_C.direction = Direction.INPUT

# Create blank image for drawing.
# Make sure to create image with mode 'RGB' for full color.
height = disp.width  # we swap height/width to rotate it to landscape!
width = disp.height
image = Image.new("RGB", (width, height))
rotation = 180

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)


# Draw a black filled box to clear the image.
draw.rectangle((0, 0, width, height), outline=0, fill=(0, 0, 0))
disp.image(image, rotation)
# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = 1
top = padding
bottom = height - padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0

# Set up a number of lines you want to show
# menu 1, 2, 3, 4, 5, 6, 7....
# answer 1, 2, 3, 4, 5, 6, 7...

line1 = top
line2 = top + 40
line3 = top + 80
line4 = top + 120
line5 = top + 160
line6 = top + 200
line7 = top + 240


def drawLines(l1, l2, l3, l4, l5, l6):
    draw.text((0, line1), l1,  font=font, fill=255)
    draw.text((0, line2), l2, font=font, fill=255)
    draw.text((0, line3), l3,  font=font, fill=255)
    draw.text((0, line4), l4,  font=font, fill=255)
    draw.text((0, line5), l5, font=font, fill=255)
    draw.text((0, line6), l6, font=font, fill=255)

# Function to do shell commands


def shell(cmd):
    return(subprocess.check_output(cmd, shell=True))


def listPayloads():
    command = "ls -F --format=single-column /home/pi/rpi/payloads"
    files = subprocess.check_output(command, shell=True)
    files = files.split("\n")
    print(files)


# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)


def start():
    # simple sub routine to show an About
    drawLines(
        "     MSK PIZERO    ",
        "",
        "Project by:",
        "GIT-MSK",
        "",
        "",
    )


def chosenItem(items):
    # Keep track of where in the item list we currentl are
    print(items[1])


global menuindex

menuItems = {
    '     MSK PIZERO   ': line1,
    'HIDScript': line2,
    'SysInfo': line3,
    'WIFI': line4,
    'About': line5,
    'Reserved': line6
}

# items = ['HIDScript', 'SysInfo', 'WIFI', 'About', 'Reserved']
# Box and text rendered in portrait mode


def menu(names, index):
    for item, placement in names.items():
        # print(item, placement)
        newKey = list(names)
        # print(newKey[index])
        if(item == newKey[index]):
            # print(item + " Is indexed!")
            draw.text((0, placement), f">{item}", font=font, fill="#ffffff")
        else:
            draw.text((0, placement), item, font=font, fill=255)


# menu(menuItems, 1)
# def menu(menustr, index):
#     global menuindex
#     font = ImageFont.load_default()
#     draw.rectangle(width, height, outline="white", fill="black")
#     for i in range(len(menustr)):
#         if(i == index):
#             menuindex = i
#             # invert(draw, 2, i*10, menustr[i])
#         else:
#             draw.text((2, i*10), menustr[i], font=font, fill=255)

# names = ['Disk', 'Memory', 'Network', 'CPUUsage', 'IPAddress', 'CODELECTRON']
# with canvas(device) as draw:
#     menu(device, draw, names, 1)
guiIndex = 1

while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # start()
    # Handling of out of bound indexes
    if(guiIndex <= 0):
        guiIndex = 5
    elif(guiIndex >= 6):
        guiIndex = 1

    menu(menuItems, guiIndex)

    # draw.text((110, 110), str(counter),  font=font, fill=255)

    if not button_A.value:
        print("A clicked")
        # command = "sudo python3 /home/pi/rpi/testkeyless.py"
        # result = subprocess.check_output(command, shell=True)
        guiIndex = 1

    if not button_D.value:  # down pressed
        print("Down")
        guiIndex += 1

    if not button_U.value:
        print("UP")
        guiIndex -= 1
    # Shell scripts for system monitoring from here:
    # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    # cmd = "hostname -I | cut -d' ' -f1"
    # IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    # cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    # CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
    # cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB  %.2f%%\", $3,$2,$3*100/$2 }'"
    # MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    # cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    # Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
    # cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}'"  # pylint: disable=line-too-long
    # Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")
    # cmd = "who | grep pts | awk {' print $2 '}"
    # SSH = subprocess.check_output(cmd, shell=True).decode("utf-8")
    # blankLine = "AAAAAAAAAAAAAAAA"

    # # Write four lines of text.
    # y = top
    # draw.text((x, y), IP, font=font, fill="#FFFFFF")
    # y += font.getsize(IP)[1]
    # draw.text((x, y), CPU, font=font, fill="#FFFF00")
    # y += font.getsize(CPU)[1]
    # draw.text((x, y), MemUsage, font=font, fill="#00FF00")
    # y += font.getsize(MemUsage)[1]
    # draw.text((x, y), Disk, font=font, fill="#0000FF")
    # y += font.getsize(Disk)[1]
    # draw.text((x, y), Temp, font=font, fill="#FF00FF")
    # y += font.getsize(blankLine)[1]
    # draw.text((x, y), blankLine, font=font, fill="#000000")
    # y += font.getsize(SSH)[1]
    # draw.text((x, y), SSH, font=font, fill="#FFFFFA")

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.1)