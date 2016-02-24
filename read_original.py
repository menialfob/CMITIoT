import nxppy
import time

mifare = nxppy.Mifare()

while True:
    try:
        uid = mifare.select()
        if uid:
                print(uid)
                x = 0
                bytesRead = []
                while True:
                        try:
                                blockBytes = mifare.read_block(x)
                                bytesRead.append(blockBytes)
                                x += 4
                        except nxppy.ReadError:
                                print("Length: {0}".format(x))
                                break
                if bytesRead:
                        ba = bytearray(''.join(bytesRead))
                        f = open(uid, 'w')
                        f.write(ba);
                        print(ba)
                        break
    except nxppy.SelectError:
        pass

    time.sleep(1)
