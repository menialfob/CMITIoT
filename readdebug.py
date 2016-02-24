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
                                print("Block attempt {}: {}".format(x,blockBytes))
                                bytesRead.append(blockBytes)
                                x += 4
                        except nxppy.ReadError:
                                print("Length: {0}".format(x))
                                break
                if bytesRead:
                        ba = bytearray('-'.join(bytesRead))
                        f = open(uid, 'w')
                        f.write(ba);
                        print(ba)
                        print("bytesRead: {}".format(bytesRead))
                        block1 = bytesRead[1]
                        block2 = bytesRead[2]
                        block3 = bytesRead[3]
                        print("1 blockBytes: " + block1)
                        print("2 blockBytes: " + block2)
                        print("3 blockBytes: " + block3)
                        print("Slice 1: " + block1[12:16])
                        print("Slice 2: " + block2[0:4])
                        print("Slice 3: " + block2[4:8])
                        print("Slice 4: " + block3)
                        
                        break
    except nxppy.SelectError:
        pass

    time.sleep(1)
