import Ngl,Nio
import math
import numpy as np
import json
import pandas as pd


fname = "/media/alley/Alley/ERA5/seasonal_analysis/1981-2019_gh_500.grib"
f = Nio.open_file(fname, 'r')
print(f.variables)
lat = np.array(f.variables['g0_lat_1'])
lon = np.array(f.variables['g0_lon_2'])
gh = np.array(f.variables['Z_GDS0_ISBL_S123'])
time = np.array(f.variables['initial_time0_encoded'])
len_time = len(time)
print(gh.shape)
n = 1
with open('1981-2019_gh_500.json', 'a', encoding='utf-8') as fout:
    for start_time_i, end_time_i in zip(range(len_time)[::12], range(len_time)[11::12]):
        for lat_i in range(len(lat)):
            for lon_i in range(len(lon)):
                tmp =  gh[start_time_i:end_time_i, lat_i, lon_i]
                tmp = [float(x) for x in tmp]
                # print(tmp)
                lat_ = float(lat[lat_i])
                lon_ = float(lon[lon_i])
                year = str(time[start_time_i])[:4]
                # print(lat_)
                # print(lon_)
                print(year)
                dic = {
                    "_id": n,
                    "loc": {"type": "Point", "coordinates": [lon_, lat_]},
                    "year": year,
                    "level": 500,
                    "gh":
                        {
                            "long_name": "Geopotential",
                            "units": "m**2 s**-2",
                            "values": tmp
                        }
                }
                dicStr = json.dumps(dic)
                fout.write(dicStr + '\n')
                n += 1
