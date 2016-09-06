


from CoordinateToRegion.getRegion import getRegion

lon = 116.65 # 经度

lat = 40.13 # 纬度

pro, city, xiangzhen = getRegion(lon, lat) # 省份、城市、乡镇

print pro, city, xiangzhen
