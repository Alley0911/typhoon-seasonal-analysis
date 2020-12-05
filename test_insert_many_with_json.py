import numpy as np
import xarray as xr
import pymongo
import datetime
import pandas as pd
import time
import json
from bson.json_util import loads

# 1. 创建数据库
client = pymongo.MongoClient('localhost', 27317)
temp = client.temp # db
t = temp.temp # collection

# 2. 获取数据信息，并插入数据
st = time.time()
filename = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/temp.json"
with open(filename, 'r', encoding='utf-8') as f:
	data = f.readlines()
	print(data)
	json = loads(data)
	print(json)
	t.insert_many(json)
et = time.time()
print(et - st)
