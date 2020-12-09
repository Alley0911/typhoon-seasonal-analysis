import pymongo
import numpy as np
import pprint
import time
import pandas as pd


st = time.time()
client = pymongo.MongoClient(host="127.0.0.1", port=27017)
tysa = client.tysa
era5 = tysa.era5


latmin = 0
latmax = 5
lonmin = 100
lonmax = 105


res = era5.find(
	{
		"loc":
		{
			"$geoWithin":
			{
				"$geometry":
				{
					"type": "Polygon",
					"coordinates": [[[lonmin, latmin], [lonmax, latmin], [lonmax, latmax], [lonmin, latmax], [lonmin, latmin]]]
				}
			}
		}
	},
	{
		"gh.values.500hPa": 1,
		"_id": 0
	}
)
data = pd.DataFrame(list(res))
print(data)


et = time.time()
print(f"耗时{et - st}s")