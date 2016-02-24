from calcdeg import *
from readfinal import *

pointerlocx  = raw_input("Please input pointer\'s x location: ")
pointerlocy  = raw_input("Please input pointer\'s y location: ")
steps = int(CalcDeg(int(pointerlocx),int(pointerlocy),int(writeoutput()[0][2]),int(writeoutput()[0][3])))/0.9
print steps
print writeoutput()[0][2]
print writeoutput()[0][3]
