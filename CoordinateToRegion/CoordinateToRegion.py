# -*- encoding: utf-8 -*-
import math
from LoadColData import LoadColData

# 获取两个经纬度之间的距离  
# <param name="LonA">经度A</param>  
# <param name="LatA">纬度A</param>  
# <param name="LonB">经度B</param>  
# <param name="LatB">经度B</param>  
# <returns>距离（千米）</returns>  

class CoordinateToRegion(object):
    def __init__(self):
        self.data = LoadColData().load()

    def _getDistance(self, (lonA, latA), (lonB, latB)):
        EARTH_RADIUS = 6378.137
        C = math.sin(self._rad(latA)) * math.sin(self._rad(latB)) + math.cos(self._rad(latA)) * math.cos(self._rad(latB)) * math.cos(self._rad(lonA - lonB))
        return (EARTH_RADIUS * math.acos(C))

    def _rad(self, angle):
        return angle * math.pi / 180.0

    def getRegion(self, lonA, latA):
        tmp = {}
        if not (lonA >= 73.55 and lonA <= 135.0084) and (latA >= 3.85 and latA <= 53.55):
            return ("国外", "国外", "国外")
        for key in self.data:
            distance = self._getDistance((lonA, latA), (key[0], key[1]))
            tmp.setdefault((key, distance), self.data[key])
        tmp_sorted = sorted(tmp.items(), key = lambda item: item[0][1], reverse = False)
        # for key in tmp_sorted:
        #     print (lonA, latA), key[0][0], key[0][1], self.data[key[0][0]][0], self.data[key[0][0]][1], self.data[key[0][0]][2]
        return self.data[tmp_sorted[0][0][0]]




if __name__ == "__main__":
    tester = CoordinateToRegion()
    a = tester.getRegion(116.65, 40.13)
    print a[0], a[1], a[2]
