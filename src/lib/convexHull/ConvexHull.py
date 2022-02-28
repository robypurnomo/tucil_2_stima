import numpy as np
from math import atan2, pi

# Mengecek letak titik pada zona atas atau bawah atau pada garis
def zoneCheck(p1, pn, p) :
    x1 = p1[0]
    x2 = pn[0]
    x3 = p[0]
    y1 = p1[1]
    y2 = pn[1]
    y3 = p[1]
    det = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3
    if det == 0 or x3 < x1 or x3 > x2 or (x3 == x1 and x3 == x2 and y3 == y1 and y3 == y2):
        return 0
    elif det > 0 :
        return 1
    else :
        return -1

# Menghitung jarak titik ke garis
def distance(pa, pb, px) :
    pa = np.array(pa)
    pb = np.array(pb)
    px = np.array(px)
    return abs(np.linalg.norm(np.cross(pb-pa, pa-px))/np.linalg.norm(pb-pa))

# Menghitung sudut diantara tiga titik
def angle(p1, pmax, pn) :
    x1, y1 = p1[0] - pmax[0], p1[1] - pmax[1]
    x3, y3 = pn[0] - pmax[0], pn[1] - pmax[1]
    a = atan2(y1, x1)
    c = atan2(y3, x3)
    if a < 0: a += pi*2
    if c < 0: c += pi*2
    return (pi*2 + c - a) if a > c else (c - a)

# ConvexHull Recursive
def ConvexHullRec(bucket, p1, pn, value) :
    idx = -1
    dis = 0
    for i in range (len(bucket)) :
        if distance(pn, p1, bucket[i]) > dis or (distance(pn, p1, bucket[i]) == dis and dis != 0 and angle(p1, bucket[i], pn) > angle(p1, bucket[idx], pn)) :
            dis = distance(pn, p1, bucket[i])
            idx = i
    if idx != -1 :
        bucketleft = []
        bucketright = []
        for i in range (len(bucket)) :
            if zoneCheck(p1, bucket[idx], bucket[i]) == value :
                bucketleft.append(bucket[i])
            if zoneCheck(bucket[idx], pn, bucket[i]) == value :
                bucketright.append(bucket[i])
        left = ConvexHullRec(bucketleft, p1, bucket[idx], value)
        right = ConvexHullRec(bucketright, bucket[idx], pn, value)
        return left + [bucket[idx]] + right
    else :
        return []

# Implementasi ConvexHull
def myConvexHull(bucket) :
    bucketlist = bucket.tolist()

    p1 = bucketlist[0]
    pn = bucketlist[0]
    for i in range(len(bucketlist)) :
        if (bucketlist[i][0] < p1[0]) :
            p1 = bucketlist[i]
        elif (bucketlist[i][0] == p1[0] and bucketlist[i][1] < p1[0]) :
            p1 = bucketlist[i]
        if (bucketlist[i][0] > pn[0]) :
            pn = bucketlist[i]
        elif (bucketlist[i][0] == pn[0] and bucketlist[i][1] > pn[0]) :
            pn = bucketlist[i]

    buckettop = []
    bucketbot = []
    for i in range (len(bucket)) :
        if zoneCheck(p1, pn, bucket[i]) == 1 :
            buckettop.append(bucket[i])
        elif zoneCheck(p1, pn, bucket[i]) == -1 :
            bucketbot.append(bucket[i])

    array_point_top = [p1]
    array_point_bot = [p1]

    top = ConvexHullRec(buckettop, p1, pn, 1)
    bot = ConvexHullRec(bucketbot, p1, pn, -1)

    array_point_top += top + [pn]
    array_point_bot += bot + [pn]
    
    x = []
    y = []

    for i in range (len(array_point_top)) :
        x.append(array_point_top[i][0])
        y.append(array_point_top[i][1])
    for i in range (len(array_point_bot)-1, -1, -1) :
        x.append(array_point_bot[i][0])
        y.append(array_point_bot[i][1])

    return x,y
