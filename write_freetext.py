import nxppy
import time

mifare = nxppy.Mifare()

# Print card UIDs as they are detected
def writetext(message):
    while True:
        try:
            uid = mifare.select()
            if uid:

                    x = 0;
                    while True:
                            try:
                                    mifare.select()
                                    mifare.read_block(x)
                                    mifare.write_block(x, message.decode('UTF-8'))
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
