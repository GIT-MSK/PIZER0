import time
import os
import subprocess
from digitalio import DigitalInOut, Direction
import board
from PIL import Image, ImageDraw, ImageFont
from adafruit_rgb_display import st7789

payloadsPath = "/home/pi/rpi/HID"

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

# Alternatively load a TTF font.  Make sure the .ttf font file is in the
# same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
font = ImageFont.truetype(
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)


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

# -------------------------------------------- Script functionality


def shell(cmd):
    return(subprocess.check_output(cmd, shell=True))


def listPayloads():

    for x in os.listdir(payloadsPath):
        if x.endswith(".py"):
            print(x)


# payloads = listPayloads()
# print(str(payloads))


def stats():
    # Shell scripts for system monitoring from here:
    # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d' ' -f1"
    IP = "IP: " + subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%s MB\", $3,$2 }'"
    MemUsage = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = 'df -h | awk \'$NF=="/"{printf "Disk: %d/%d GB  %s", $3,$2,$5}\''
    Disk = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}'"  # pylint: disable=line-too-long
    Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")
    cmd = "who | grep pts | awk {' print $2 '}"
    SSH = subprocess.check_output(cmd, shell=True).decode("utf-8")
    blankLine = "AAAAAAAAAAAAAAAA"

    # Draw the text to the screen
    y = top
    draw.text((x, y), IP, font=font, fill="#FFFFFF")
    y += font.getsize(IP)[1]
    draw.text((x, y), CPU, font=font, fill="#FFFF00")
    y += font.getsize(CPU)[1]
    draw.text((x, y), MemUsage, font=font, fill="#00FF00")
    y += font.getsize(MemUsage)[1]
    draw.text((x, y), Disk, font=font, fill="#0000FF")
    y += font.getsize(Disk)[1]
    draw.text((x, y), Temp, font=font, fill="#FF00FF")
    y += font.getsize(blankLine)[1]
    draw.text((x, y), blankLine, font=font, fill="#000000")
    y += font.getsize(SSH)[1]
    draw.text((x, y), SSH, font=font, fill="#FFFFFA")


def shutdown():
    print("shutting down")
    command = "/usr/bin/sudo /sbin/shutdown -h now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)


# -------------------------------------------- Pages

def drawLines(l1, l2, l3, l4, l5, l6):
    draw.text((0, line1), l1,  font=font, fill=255)
    draw.text((0, line2), l2, font=font, fill=255)
    draw.text((0, line3), l3,  font=font, fill=255)
    draw.text((0, line4), l4,  font=font, fill=255)
    draw.text((0, line5), l5, font=font, fill=255)
    draw.text((0, line6), l6, font=font, fill=255)

# Does currently not work correctly with over 6 items


def about():
    # simple sub routine to show an About
    drawLines(
        "     MSK PIZERO    ",
        "",
        "For education",
        "",
        "Project by:",
        "-MSK-",
    )


menuItems = {
    '     MSK PIZERO   ': line1,
    'HIDScript': line2,
    'SysInfo': line3,
    'WIFI': line4,
    'About': line5,
    'Shutdown': line6
}

wifiItems = {
    '           WIFI       ': line1,
    'Show WIFIS': line2,
    'MITM': line3,
    'DeAuther': line4,
    'GetHash': line5,
    # 'Shutdown': line6
}


# -------------------------------------------- Menu functions

# Makes a text based GUI menu that shows your current pos >MenuItem

def mainMenu(names, index):
    for item, placement in names.items():
        # print(item, placement)
        newKey = list(names)
        # print(newKey[index])
        if(item == newKey[index]):
            # print(item + " Is indexed!")
            draw.text((0, placement), f">{item}", font=font, fill="#ffffff")
        else:
            draw.text((0, placement), item, font=font, fill=255)

# Finds the current selected menuitem and returns in


def findMainMenuItem(names, index):
    for item, placement in names.items():
        # print(item, placement)
        newKey = list(names)
        # print(newKey[index])
        if(item == newKey[index]):
            print(item + " Is indexed!")
            return item


def drawDynamicLines(list, index):
    pos = top + 40
    for x in list:

        if(x == list[index]):
            draw.text((0, pos), f">{x}", font=font, fill="#ffffff")
        else:
            draw.text((0, pos), x, font=font, fill=255)

        pos += 40

# Indexing the list, making it scrollable by looking for what the current guiIndex is


def indexItems(list, guiIndex):

    # Assumes theres is a title in line 1
    if(guiIndex <= 0):
        guiIndex = len(list) - 1
    elif(guiIndex >= len(list)):
        guiIndex = 1

    return guiIndex

# Indexing of files (or items) , with pages that does not have titles

def indexFiles(list, guiIndex):

    # Assumes theres is a title in line 1
    if(guiIndex < 0):
        guiIndex = len(list) - 1
    elif(guiIndex >= len(list)):
        guiIndex = 0

    return guiIndex

# Global ?


guiIndex = 1
menuIndex = 1

# The entire menu system needs a cleanup, python switch case when?


while True:
    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Handling of buttons to scroll up and down the list of items
    if not button_D.value:  # down pressed
        guiIndex += 1

    if not button_U.value:
        guiIndex -= 1

    if not button_A.value:
        # command = "sudo python3 /home/pi/rpi/testkeyless.py"
        # result = subprocess.check_output(command, shell=True)
        guiIndex = 1
        menuIndex = 1

    # Control of what menu we are currently in
    if(menuIndex == 1):

        guiIndex = indexItems(menuItems, guiIndex)
        mainMenu(menuItems, guiIndex)

        if not button_B.value:

            indexedItem = findMainMenuItem(menuItems, guiIndex)

            # Find a clean way to do this for all menu items

            if(indexedItem == "HIDScript"):
                menuIndex = 2
            elif(indexedItem == "SysInfo"):
                menuIndex = 3
            elif(indexedItem == "WIFI"):
                menuIndex = 4
            elif(indexedItem == "About"):
                menuIndex = 5
            elif(indexedItem == "Shutdown"):
                shutdown()
    # HID Scripts
    elif(menuIndex == 2):

        payloadList = os.listdir(payloadsPath)

        guiIndex = indexFiles(payloadList, guiIndex)

        drawDynamicLines(payloadList, guiIndex)

    # SysInfo
    elif(menuIndex == 3):
        stats()

    # Wifi menu
    elif(menuIndex == 4):

        guiIndex = indexItems(wifiItems, guiIndex)
        mainMenu(wifiItems, guiIndex)

    # About page
    elif(menuIndex == 5):
        about()

        if not button_A.value:
            # command = "sudo python3 /home/pi/rpi/testkeyless.py"
            # result = subprocess.check_output(command, shell=True)
            menuIndex = 1

    # Display image.
    disp.image(image, rotation)
    time.sleep(0.01)
