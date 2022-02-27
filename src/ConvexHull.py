import numpy as np
import pandas as pd 
from sklearn import datasets 
from scipy.spatial import ConvexHull


# Mengecek letak titik pada zona atas atau bawah atau pada garis
def zoneCheck(p1, pn, p) :
    x1 = p1[0]
    x2 = pn[0]
    x3 = p[0]
    y1 = p1[1]
    y2 = pn[1]
    y3 = p[1]
    det = x1*y2 + x3*y1 + x2*y3 - x3*y2 - x2*y1 - x1*y3
    if det == 0 :
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

# ConvexHull untuk bagian Top
def ConvexHullTop(bucket, p1, pn) :
    x1 = p1[0]
    x2 = pn[0]
    y1 = p1[1]
    y2 = pn[1]
    idx = -1
    dis = 0
    for i in range (len(bucket)) :
        x = bucket[i][0]
        y = bucket[i][1]
        if zoneCheck(p1, pn, bucket[i]) == 1 and distance(pn, p1, bucket[i]) > dis and (x >= x1 and x <= x2) and not (x == x1 and x == x2 and y == y1 and y == y2):
            dis = distance(pn, p1, bucket[i])
            idx = i
    if idx != -1 :
        left = ConvexHullTop(bucket, p1, bucket[idx])
        right = ConvexHullTop(bucket, bucket[idx], pn)
        return left + [bucket[idx]] + right
    else :
        return []

# ConvexHull untuk bagian Bot
def ConvexHullBot(bucket, p1, pn) :
    x1 = p1[0]
    x2 = pn[0]
    y1 = p1[1]
    y2 = pn[1]
    idx = -1
    dis = 0.01
    
    for i in range (len(bucket)) :
        x = bucket[i][0]
        y = bucket[i][1]
        if (distance(p1, pn, bucket[i]) > dis and zoneCheck(p1, pn, bucket[i]) == -1 ) and (x >= x1 and x <= x2) and not (x == x1 and x == x2 and y == y1 and y == y2):
            dis = distance(p1, pn, bucket[i])
            idx = i
    if idx != -1 :
        left = ConvexHullBot(bucket, p1, bucket[idx])
        right = ConvexHullBot(bucket, bucket[idx], pn)
        return left + [bucket[idx]] + right
    else :
        return []

# Implementasi ConvexHull
def ConvexHull(bucket) :
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

    array_point_top = [p1]
    array_point_bot = [p1]

    top = ConvexHullTop(bucket, p1, pn)
    bot = ConvexHullBot(bucket, p1, pn)

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