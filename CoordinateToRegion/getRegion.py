from CoordinateToRegion import CoordinateToRegion


global ctr
ctr = CoordinateToRegion()

def getRegion(lon, lat):
    return ctr.getRegion(lon, lat)



if __name__ == "__main__":
    print getRegion(116.65, 40.13)
