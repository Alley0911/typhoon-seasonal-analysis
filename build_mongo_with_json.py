import numpy as np
import xarray as xr
import pymongo
import datetime
import pandas as pd
import time
import json


# 1. 创建数据库
client = pymongo.MongoClient('localhost', 27317)
tysa = client.tysa # db
era5 = tysa.era5 # collection

# 2. 获取数据信息，并插入数据
st = time.time()
n = 1
filename = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/1981-2019_gh_500_by_only_latlon.json"
with open(filename, 'r', encoding='utf-8') as f:
    for i in f:
        print(n)
        data = json.loads(i)
        era5.insert_one(data)
        n += 1
et = time.time()
print(et - st)
