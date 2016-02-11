import math

def Calculatedegrees(basex,basey,tarx,tary):
    distancex = basex - tarx
    distancey = tary - basey
    if distancex > 0 and distancey > 0:
        hypotenuse = math.sqrt(math.pow(distancex,2)+math.pow(distancey,2))
        degrees = 270 + math.degrees(math.acos(distancex/hypotenuse))
        return degrees
    if distancex > 0 and distancey < 0:
        distancey = basey - tary
        hypotenuse = math.sqrt(math.pow(distancex,2)+math.pow(distancey,2))
        degrees = 180 + math.degrees(math.acos(distancey/hypotenuse))
        return degrees
    if distancex < 0 and distancey > 0:
        distancex = tarx - basex
        hypotenuse = math.sqrt(math.pow(distancex,2)+math.pow(distancey,2))
        degrees = math.degrees(math.acos(distancey/hypotenuse))
        return degrees
    if distancex < 0 and distancey < 0:
        distancex = tarx - basex
        distancey = basey - tary
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
    else:
        print("Error: Outside of calculation scenario")
