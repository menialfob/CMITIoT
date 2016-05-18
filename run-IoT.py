from CalculateDegrees import *
from read import *

pointerlocx  = raw_input("Please input pointer\'s x location: ")
pointerlocy  = raw_input("Please input pointer\'s y location: ")
print 'Scan tag please:'
steps = int(CalcDeg(int(pointerlocx),int(pointerlocy),int(writeoutput()[0][0:4]),int(writeoutput()[1][0:4])))/0.9
print ('Steppermotor will move {0} steps'.format(steps))
print writeoutput()[0][0:4]
print writeoutput()[1][0:4]
