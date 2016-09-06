# coding: utf-8
import os

from __init__ import base_path


class LoadColData(object):
    def __init__(self):
        self.data_path = os.sep.join([base_path, "coordinate.data"])
        # self.data_path = "/data/py/CoordinateToRegion/coordinate.data"

    def load(self):
        result = {}
        with open(self.data_path) as f:
            for line in f.readlines():
                if line.startswith("#"):
                    continue
                try:
                    items = line.split("\t")
                    pro = items[0].strip()
                    city = items[1].strip()
                    county = items[2].strip()
                    lon = float(items[3].strip())
                    lat = float(items[4].strip())
                except:
                    continue
                result.setdefault((lon, lat), (pro, city, county))
        return result

if __name__ == "__main__":
    # tester = LoadColData()
    # print tester.load()
    print LoadColData().load()
