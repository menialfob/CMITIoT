from functools import partial
import nxppy
import os
import time

mifare = nxppy.Mifare()

# Print card UIDs as they are detected
def writetext(message):
    while True:
        try:
            uid = mifare.select()
            if uid and os.path.isfile(uid):

                    f = open(uid)
                    x = 0;
                    for block in iter(partial(f.read, 4), ''):
                            try:
                                    mifare.select()
                                    mifare.read_block(x)
                                    mifare.write_block(x, bytes(message))
                                    print('{0}: Write succeeded'.format(x))
                            except nxppy.WriteError as e:
                                    print('{0}: {1}'.format(x, e))
                            except nxppy.ReadError:
                                    break
                            x += 1
                    print('Wrote {0} blocks'.format(x))
                    break
        except nxppy.SelectError:
            pass

        time.sleep(1)
textinput = raw_input("Please enter text to write:")
writetext(str(textinput))
