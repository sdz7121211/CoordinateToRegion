# -*- encoding: utf-8-*-
from CoordinateToRegion.CoordinateToRegion.CoordinateToRegion import getRegion

# 经度
lon = 116.65
# w纬度
lat = 40.13


#s省份、城市、乡镇
pro, city, xiangzhen = getRegion(lon, lat)
print pro, city, xiangzhen
