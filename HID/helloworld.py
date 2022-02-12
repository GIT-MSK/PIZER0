from HIDmsk import *


def main():
    outputHoldMod('GUI', 'R')

    time.sleep(1)

    writeString("notepad.exe")

    time.sleep(1)

    outputChar("ENTER")

    time.sleep(2)

    for i in range(5):
        writeString("Hello From RP Zero 2 W!\n")


main()
