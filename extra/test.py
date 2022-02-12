
from extra.HIDmsk import *


def main():
    outputHoldMod('KEY_GUI', 'KEY_R')

    time.sleep(1)

    writeString("notepad.exe")

    time.sleep(2)

    outputChar("KEY_ENTER")

    time.sleep(2)

    writeString("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse pharetra, sem sit amet lacinia dapibus, magna enim auctor ligula, viverra convallis erat sem eget justo. Duis tempor blandit tristique. Nulla consectetur euismod urna ut pellentesque. Fusce at lobortis dolor, quis posuere nunc. Vestibulum in lacinia leo. Sed at aliquam tortor, in commodo lectus. Sed vestibulum ipsum et ligula tempor consequat. Nullam non diam vel diam commodo mattis eget in elit. Vivamus semper bibendum mauris, eget maximus tellus molestie ac. Suspendisse porta rhoncus suscipit. Sed convallis tempor dolor, eget eleifend tortor imperdiet ac. Duis at elit non enim aliquet dictum.\nCurabitur semper urna turpis. Fusce in magna ut nisi finibus vehicula. Etiam ut dui vel massa facilisis pellentesque sit amet sed odio. Quisque fermentum imperdiet arcu vel commodo. Duis laoreet tristique volutpat. Maecenas eget est faucibus, molestie nisl sit amet, accumsan nulla. Maecenas sodales eros eget ipsum maximus pulvinar. Maecenas congue tempor libero auctor mattis. Maecenas sit amet pulvinar ante, sit amet varius massa.\nPellentesque fringilla lacinia nulla at ornare. Suspendisse nec mollis elit. Sed at imperdiet ipsum. Etiam at volutpat quam, id sodales leo. Nam quis lorem nec diam ullamcorper volutpat. Nam et ullamcorper eros. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam tristique ut nisi ut placerat. Donec malesuada vulputate commodo. Nam faucibus, nulla ac tempor semper, neque massa ullamcorper dui, sed mollis metus ante non ipsum. Ut sapien dolor, auctor ac ornare sed, pellentesque vitae odio. Proin quis lectus ornare, egestas leo nec, aliquet dolor.\nMauris quam purus, volutpat in erat et, gravida ultrices eros. Donec tortor turpis, commodo sit amet sagittis sed, tempor ut tellus. Nam tristique nec nibh vel molestie. Aliquam tincidunt ex ipsum, ut rhoncus dui placerat non. Praesent velit quam, pellentesque vel ipsum eget, venenatis pulvinar tortor. Sed vitae vulputate est. Nunc elementum risus massa, sed condimentum odio placerat at. Fusce vitae mattis arcu. Etiam vehicula dui ornare elit ultrices, quis accumsan mauris interdum. Nullam iaculis at nunc at facilisis. Nunc eu purus euismod, commodo augue eu, bibendum quam. Quisque dictum at ex nec pellentesque. Nulla tincidunt iaculis sagittis. Praesent eu nunc molestie, malesuada arcu sed, sodales sem. Nullam cursus bibendum mollis.\nClass aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Phasellus pretium bibendum pulvinar. Cras porttitor hendrerit quam, nec mattis ante bibendum ac. Donec elit dui, porttitor aliquam quam ac, tristique tempor nisl. Cras aliquam suscipit mauris id interdum. Proin accumsan est metus. In pharetra aliquam nisl, ut consectetur ligula sodales ut. Integer mattis sapien ac ex interdum, a vehicula arcu accumsan.")

    writeString("Hello From RP Zero 2 W!")


main()
