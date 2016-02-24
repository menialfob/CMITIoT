import nxppy
import time

mifare = nxppy.Mifare()

# Print card UIDs as they are detected
while True:
    try:
        uid = mifare.select()
        if uid:
                writelist = ["sec1","sec2","sec3","sec4","sec5","sec6","sec7","sec8","sec9","se10","se11","se12","se13","se14","se15","se16"]
                x = 0;
                for sector in writelist:
                        try:
                                mifare.select()
                                mifare.read_block(x)
                                mifare.write_block(x, writelist[x].decode('UTF-8'))
                                print('{0}: Write succeeded'.format(writelist[x]))
                        except nxppy.WriteError as e:
                                print('{0}: {1}'.format(writelist[x], e))
                        except nxppy.ReadError:
                                break
                        x += 1
                print('Wrote {0} blocks'.format(x))
                break
    except nxppy.SelectError:
        pass

    time.sleep(1)
