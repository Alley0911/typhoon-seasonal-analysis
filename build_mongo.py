import numpy as np
import xarray as xr
import pymongo
import datetime
import pandas as pd
import time
import json


# 1. 创建数据库
client = pymongo.MongoClient()
seasonal_analysis = client.seasonal_analysis # db
era5 = seasonal_analysis.era5 # collection

# 2. 获取数据信息，并插入数据
filename = "/media/alley/Alley/ERA5/seasonal_analysis/1981-2019_gh_500.grib"
ds = xr.open_dataset(filename, engine="cfgrib")
date = ds.coords['time']
lat = ds.coords['latitude'].values
lon = ds.coords['longitude'].values
# level = ds.coords['isobaricInhPa'].values
st = time.time()
n = 1
with open('1981-2019_gh_500.json', 'a', encoding='utf-8') as fout:
    for lat_ in lat:
        for lon_ in lon:
            for start_time, end_time in zip(date[0::12], date[11::12]):
                print(start_time.values)
                print(end_time.values)
                tmp = ds["z"].loc[dict(time=slice(start_time, end_time), latitude=lat_, longitude=lon_)]
                tmp = [float(x) for x in(tmp.values)]
                lat_ = float(lat_)
                lon_ = float(lon_)
                year_ = int(start_time.dt.year.values)
                level_ = 500
                dic = {
                        "_id" : n,
                        "loc":{"type": "Point", "coordinates": [lon_, lat_]},
                        "year": year_,
                        "level": level_,
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

            # break
        # break


et = time.time()
print(et - st)
