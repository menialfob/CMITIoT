from math import atan2, degrees, pi

def CalcDeg(x1,y1,x2,y2):
    dx = x2 - x1
    dy = y2 - y1
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)
    return degs
