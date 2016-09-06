
According to the latitude and longitude into place names, only to support the transformation of the latitude and longitude of china.

根据经纬度转化为地名，仅支持中国境内的经纬度转化。

from CoordinateToRegion.getRegion import getRegion

lon = 116.65 # 经度

lat = 40.13 # 纬度

pro, city, xiangzhen = getRegion(lon, lat) # 省份、城市、乡镇

print pro, city, xiangzhen


# First

git clone https://github.com/sdz7121211/CoordinateToRegion

copy CoordinateToRegion to your project path.
