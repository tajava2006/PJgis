from geojson import load, LineString, Point, Feature
from turfpy import measurement
from math import inf




def getOrthogonalCoordinates(st, en, target):

    # 경도와 위도로 표현된 두 점 st, en을 끝점으로 하는 구좌표계 위 선분에 target 에서부터 수선을 긋고 수선의 발의 경도와 위도를 리턴

    x1 = st[0]
    y1 = st[1]
    x2 = en[0]
    y2 = en[1]
    x3 = target[0]
    y3 = target[1]

    xx = x2 - x1 
    yy = y2 - y1 
    temp = ((xx * (x3 - x1)) + (yy * (y3 - y1))) / ((xx * xx) + (yy * yy)) 
    X4 = x1 + xx * temp 
    Y4 = y1 + yy * temp
    return X4,Y4
    


# 주어진 geojson 파일을 열어 geojson 객체(FeatureCollection)로 담는다
file = open('links.geojson')
gis = load(file)

# 경도와 위도를 입력으로 받아 geojson의 점 객체로 만든다
point = Feature(geometry = Point(list(map(float,input().split(',')))))


# 정답을 담을 변수들을 선언한다. 여기서 한 가지 유의할 점은 link와 target의 사이각이 90도를 넘어간다면 수선의 발이 link에 포함되지 않을 수 있다는 점이다. 때문에 distToLink는 선분의 끝 점과 target사이의 거리가 되고 answer는 수선의 발 사이와 target 사이의 거리가 되어서 다를 수 있다.
ansLng = None
ansLat = None
distToLink = inf
answer = 0




# gis 객체 안에 있는 모든 feature를 돌면서 target 와의 거리를 측정한다
for feature in gis.features:
    # 각각의 feature가 단순한 line이 아니라 lineString이기 때문에 해당 feature의 crrodinates의 인접한 두 좌표를 두 끝점으로 하는 line(=link)와 target과의 거리를 측정한다
    for i in range(len(feature.geometry.coordinates)-1):
        p1 = feature.geometry.coordinates[i]
        p2 = feature.geometry.coordinates[i+1]  
        line = []
        line.append(p1)
        line.append(p2)


        # 두 점만으로 이루어진 단순한 lineString 객체를 선언해준다
        temp = Feature(geometry = LineString(line))

        # 만들어진 lineString와 target사이의 거리를 turfpy 모듈을 이용하여 측정한다
        distance = measurement.point_to_line_distance(point,temp)

        # 측정된 거리가 이제까지의 측정된 최소거리 보다 짧다면 정답을 갱신한다
        if distance < distToLink:

            distToLink = distance
            
            # 수선의 발 H의 경위도를 계산한다
            ansLng, ansLat = getOrthogonalCoordinates(p1,p2,point.geometry.coordinates)
            
            # 수선의 발 H의 geojson 객체를 생성한다
            h = Feature(geometry = Point((ansLng, ansLat)))
            
            # target와 H의 거리를 계산한다.
            answer = measurement.distance(point, h, units='m')

print(str(answer) + ', ' + str(ansLng) + ', ' + str(ansLat))

