from math import atan2, degrees, pi

def CalcDeg(xy1,xy2):
    dx = xy2[0] - xy1[0]
    dy = xy2[1] - xy1[1]
    rads = atan2(-dy,dx)
    rads %= 2*pi
    degs = degrees(rads)

    return degs
