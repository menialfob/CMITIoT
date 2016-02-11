
# coding: utf-8

# In[3]:

import math

def Calculatedegrees(basecor,tarcor):
    distancex = basecor[0] - tarcor[0]
    distancey = tarcor[1] - basecor[1]
    if distancex > 0 and distancey > 0:
        hypotenuse = math.sqrt(math.pow(distancex,2)+math.pow(distancey,2))
        degrees = 270 + math.degrees(math.acos(distancex/hypotenuse))
        return degrees
    if distancex > 0 and distancey < 0:
        distancey = basecor[1] - tarcor[1]
        hypotenuse = math.sqrt(math.pow(distancex,2)+math.pow(distancey,2))
        degrees = 180 + math.degrees(math.acos(distancey/hypotenuse))
        return degrees
    if distancex < 0 and distancey > 0:
        distancex = tarcor[0] - basecor[0]
        hypotenuse = math.sqrt(math.pow(distancex,2)+math.pow(distancey,2))
        degrees = math.degrees(math.acos(distancey/hypotenuse))
        return degrees
    if distancex < 0 and distancey < 0:
        distancex = tarcor[0] - basecor[0]
        distancey = basecor[1] - tarcor[1]
        hypotenuse = 90 + math.sqrt(math.pow(distancex,2)+math.pow(distancey,2))
        degrees = math.degrees(math.acos(distancex/hypotenuse))
        return degrees
    if distancex == 0 and distancey > 0:
        degrees = 0
        return degrees
    if distancex == 0 and distancey < 0:
        degrees = 180
        return degrees
    if distancex > 0 and distancey == 0:
        degrees = 270
        return degrees
    if distancex < 0 and distancey == 0:
        degrees = 90
        return degrees
Calculatedegrees((11,2),(14,8))


# In[ ]:



