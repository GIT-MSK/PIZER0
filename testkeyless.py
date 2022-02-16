
from HID.HIDmsk import outputChar, writeString, outputHoldMod, outputMod
import time


def main():
    outputHoldMod('GUI', 'R')

    time.sleep(1)

    writeString("notepad.exe")

    time.sleep(2)

    outputChar("ENTER")

    time.sleep(2)

    writeString("Lorem ipsum dolor sit amet, consectetur adipiscing elit. \nSuspendisse pharetra, sem sit amet lacinia dapibus, magna enim auctor ligula, viverra convallis erat sem eget justo. \nDuis tempor blandit tristique. \nNulla consectetur euismod urna ut pellentesque. \nFusce at lobortis dolor, quis posuere nunc. \nVestibulum in lacinia leo. \nSed at aliquam tortor, in commodo lectus. \nSed vestibulum ipsum et ligula tempor consequat. \nNullam non diam vel diam commodo mattis eget in elit. \nVivamus semper bibendum mauris, eget maximus tellus molestie ac. \nSuspendisse porta rhoncus suscipit. \nSed convallis tempor dolor, eget eleifend tortor imperdiet ac. \nDuis at elit non enim aliquet dictum.\nCurabitur semper urna turpis. \nFusce in magna ut nisi finibus vehicula. \nEtiam ut dui vel massa facilisis pellentesque sit amet sed odio. \nQuisque fermentum imperdiet arcu vel commodo. \nDuis laoreet tristique volutpat. \nMaecenas eget est faucibus, molestie nisl sit amet, accumsan nulla. \nMaecenas sodales eros eget ipsum maximus pulvinar. \nMaecenas congue tempor libero auctor mattis. \nMaecenas sit amet pulvinar ante, sit amet varius massa.\nPellentesque fringilla lacinia nulla at ornare. \nSuspendisse nec mollis elit. \nSed at imperdiet ipsum. \nEtiam at volutpat quam, id sodales leo. \nNam quis lorem nec diam ullamcorper volutpat. \nNam et ullamcorper eros. \nLorem ipsum dolor sit amet, consectetur adipiscing elit. \nEtiam tristique ut nisi ut placerat. \nDonec malesuada vulputate commodo. \nNam faucibus, nulla ac tempor semper, neque massa ullamcorper dui, sed mollis metus ante non ipsum. \nUt sapien dolor, auctor ac ornare sed, pellentesque vitae odio. \nProin quis lectus ornare, egestas leo nec, aliquet dolor.\nMauris quam purus, volutpat in erat et, gravida ultrices eros. \nDonec tortor turpis, commodo sit amet sagittis sed, tempor ut tellus. \nNam tristique nec nibh vel molestie. \nAliquam tincidunt ex ipsum, ut rhoncus dui placerat non. \nPraesent velit quam, pellentesque vel ipsum eget, venenatis pulvinar tortor. \nSed vitae vulputate est. \nNunc elementum risus massa, sed condimentum odio placerat at. \nFusce vitae mattis arcu. \nEtiam vehicula dui ornare elit ultrices, quis accumsan mauris interdum. \nNullam iaculis at nunc at facilisis. \nNunc eu purus euismod, commodo augue eu, bibendum quam. \nQuisque dictum at ex nec pellentesque. \nNulla tincidunt iaculis sagittis. \nPraesent eu nunc molestie, malesuada arcu sed, sodales sem. \nNullam cursus bibendum mollis.\nClass aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. \nPhasellus pretium bibendum pulvinar. \nCras porttitor hendrerit quam, nec mattis ante bibendum ac. \nDonec elit dui, porttitor aliquam quam ac, tristique tempor nisl. \nCras aliquam suscipit mauris id interdum. \nProin accumsan est metus. \nIn pharetra aliquam nisl, ut consectetur ligula sodales ut. \nInteger mattis sapien ac ex interdum, a vehicula arcu accumsan.")

    writeString("Hello From RP Zero 2 W!")


if __name__ == '__main__':
    main()
