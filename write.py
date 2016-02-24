import nxppy
import time

mifare = nxppy.Mifare()

def writeinput(message1,message2,message3,message4):

    while True:
        try:
            uid = mifare.select()
            if uid:
                    sectorlist = [7,8,9,15]
                    messagelist = []
                    messagelist.append(message1)
                    messagelist.append(message2)
                    messagelist.append(message3)
                    messagelist.append(message4)
                    x = 0
                    for sector in sectorlist:
                            try:
                                    mifare.select()
                                    mifare.read_block(sector)
                                    mifare.write_block(sector, messagelist[x].decode('UTF-8'))
                                    print('Sector {0}: Write succeeded'.format(sector))
                                    x += 1
                            except nxppy.WriteError as e:
                                    print('{0}: {1}'.format(sector, e))
                            except nxppy.ReadError:
                                    break
                    print('Wrote 4 blocks')
                    break
        except nxppy.SelectError:
            pass

        time.sleep(1)
