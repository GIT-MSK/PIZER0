from hidtest.HIDmsk import outputHoldMod
import time
import sys
import os

sys.path.insert(0, '/home/pi/rpi/hidtest')
# sys.path.append(os.getcwd())


def main():

    outputHoldMod('GUI', 'R')

    time.sleep(1)

    # writeString("notepad.exe")

    # time.sleep(1)

    # outputChar("ENTER")

    # time.sleep(2)

    # for i in range(5):
    #     writeString("Hello From RP Zero 2 W!\n")


if __name__ == '__main__':
    main()
