# PJgis

geojson 데이터 파일 경로와 target를 입력받아 target에서 가장 가까운 링크까지의 거리와 링크까지의 수선의 발의 좌표를 리턴합니다.

해당 프로그램은 turfpy와 geojson 두 라이브러리에 의존합니다.

pyinstaller를 이용하여 실행파일을 만들었기에

./findlink -links links.geojson -target 127.027268062,37.499212063

와 같이 작동하지만 맥북에서는 작동하지 않습니다.

~~맥북에서는 python이 설치되어 있어야 하고 turfpy와 geojson 두 라이브러리를 pip를 통해 설치해주시고

~~python3 findlink.py -links links.geojson -target 127.027268062,37.499212063

~~라는 방식을 통해 실행시켜주시기 바랍니다.

-> go를 이용한 프로그램을 사용하여 주시기 바랍니다.
https://github.com/tajava2006/PJgis_go

