
from HIDmsk import *


def main():
    outputHoldMod('KEY_GUI', 'KEY_R')

    time.sleep(1)

    writeString("firefox http://")

    time.sleep(1)

    outputChar("KEY_ENTER")

    time.sleep(1)

    writeString("Hello From RP Zero 2 W!")


main()
