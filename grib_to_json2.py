import Ngl,Nio
import math
import numpy as np
import json
import pandas as pd
import datetime
import time


st = time.time()
fname = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/1981-2019_gh_500.grib"
f = Nio.open_file(fname, 'r')
# print(f.variables)
lat = np.array(f.variables['g0_lat_1'])
lon = np.array(f.variables['g0_lon_2'])
Time = list(np.array(f.variables['initial_time0_encoded']))
gh = np.array(f.variables['Z_GDS0_ISBL_S123'])
dims = (gh.shape)
print(dims)
n = 0
with open('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/1981-2019_gh_500_by_only_latlon.json', 'w', encoding='utf-8') as fout:
    for lat_i in range(len(lat)):
        for lon_i in range(len(lon)):
            tmp = (gh[:, lat_i, lon_i])
            tmp = (np.array(tmp).reshape(int(dims[0]/12), 12)).tolist() # 维度（年数，月数）
            lat_ = float(lat[lat_i])
            lon_ = float(lon[lon_i])
            dic = {
                "_id": n,
                "loc": {"type": "Point", "coordinates": [lon_, lat_]},
                "gh":
                    {
                        "time": Time,
                        "level": ["500hPa"],
                        "long_name": "Geopotential",
                        "units": "m**2 s**-2",
                        "values": {"500hPa":tmp}
                    }
            }
            dicStr = json.dumps(dic)
            fout.write(dicStr + '\n')
            n += 1
            print(n)
et = time.time()
ct = et - st
print(f"cost{ct}s")