import pymongo
import gridfs
import Nio,Ngl
from gridfs_ import *
import time
import os


# latmin = 0
# latmax = 60
# lonmin = 90
# lonmax = 180
# anomaly = True
# month = [11]
localPath = '/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/'
cli = "cli/"
cur = "cur/"

class plt_contour_500hPa(object):
	"""docstring for plt_contour_500hPa"""
	def __init__(self, latmin, latmax, lonmin, lonmax, year, month, anomaly):
		self.latmin = latmin
		self.latmax = latmax
		self.lonmin = lonmin
		self.lonmax = lonmax
		self.anomaly = anomaly
		self.month = month
		self.year = year


	def getFileNames(self):
		filenames = []
		if self.anomaly:
			years = list(range(1981, 2011))
			years.append(self.year)
			for year in years:
				tmp = "gh_500_" + str(year) + str(self.month).zfill(2) + ".grb"
				filenames.append(tmp)
		else:
			tmp = "gh_500_" + str(self.year) + str(self.month).zfill(2) + ".grb"
			filenames.append(tmp)
		return filenames

	# def draw():

if __name__ == '__main__':
	a = plt_contour_500hPa(0, 60, 100, 180, 2019, 11, True)
	filenames = ((a.getFileNames()))
		
	fs = MongoGridFS("gridfs")
	st = time.time()
	for file in filenames[:-1]:
		print(file)
		if not os.path.exists(localPath + cli + file):
			fs.downLoadFile("fs", file, localPath + cli + file, -1)
	for file in filenames[-1:]:
		print(file)
		if not os.path.exists(localPath + cur + file):
			fs.downLoadFile("fs", file, localPath + cur + file, -1)
	et = time.time()
	print(f"Totol time:{et - st:.4}")
# f = Nio.open_file(filename, 'r')
# print((f.variables))