import geojson as gj
from geojson import LineString, Point, Feature
from turfpy.measurement import point_to_line_distance
from math import inf
from decimal import Decimal

def getOrthogonalCoordinates(st, en, target):

    x1 = st[0]
    y1 = st[1]
    x2 = en[0]
    y2 = en[1]
    x3 = target[0]
    y3 = target[1]

    xx = x2 - x1 
    yy = y2 - y1 
    ShortestLength = ((xx * (x3 - x1)) + (yy * (y3 - y1))) / ((xx * xx) + (yy * yy)) 
    X4 = x1 + xx * ShortestLength 
    Y4 = y1 + yy * ShortestLength
    return X4,Y4
    



file = open('links.geojson')
gis = gj.load(file)


point = Feature(geometry=Point(list(map(float,input().split(',')))))

print(point)

ansLng = None
ansLat = None
minDist = inf




for feature in gis.features:
    for i in range(len(feature.geometry.coordinates)-1):
        p1 = feature.geometry.coordinates[i]
        p2 = feature.geometry.coordinates[i+1]  
        line = []
        line.append(p1)
        line.append(p2)


        # print(line)

        temp = Feature(geometry=LineString(line))

        # print(temp)


        distance = point_to_line_distance(point,temp)


        if distance < minDist:
            minDist = distance
            ansLng, ansLat = getOrthogonalCoordinates(p1,p2,point.geometry.coordinates)

print(minDist*1000,ansLng,ansLat)

