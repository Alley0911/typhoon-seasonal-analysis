import pymongo
import gridfs
import Nio,Ngl
from gridfs_ import *
import time
import os
import multiprocessing
from frequency import draw_frequency
from draw_gh_500 import draw_gh_500hPa
from draw_uv_850_200 import draw_uv
from draw_sst import draw_sst 


localPath = '/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/'
cli = "cli/"
cur = "cur/"

class GetData(object):
    """docstring for GetData"""
    def __init__(self, year, month):
        self.month = month
        self.year = year


    def getFileNames(self, prefix):
        filenames = []
        years = list(range(1981, 2011))
        years.append(self.year)
        for year in years:
            tmp = prefix + str(year) + str(self.month).zfill(2) + ".grb"
            filenames.append(tmp)
        return filenames

    # def draw():

if __name__ == '__main__':
    sel_year = int(input("please input the year to analyse:"))
    sel_month = int(input("please input the month to analyse:"))
    print(sel_year)
    print(sel_month)

    a = GetData(sel_year, sel_month)
    fs = MongoGridFS("gridfs")

    st = time.time()
    for prefix in ["sst_", "uv_850_200_", "gh_500_"]:
        filenames = ((a.getFileNames(prefix)))        
        for file in filenames[:-1]:
            print(file)
            if not os.path.exists(localPath + cli + file):
                fs.downLoadFile("fs", file, localPath + cli + file, -1)
        for file in filenames[-1:]:
            print(file)
            if not os.path.exists(localPath + cur + file):
                fs.downLoadFile("fs", file, localPath + cur + file, -1)
   
    et1 = time.time()
    print(f"Downloding files takes {et1 - st:.2}s")

    th_fre = multiprocessing.Process(target=draw_frequency, args=((sel_year,)))    
    th_sst = multiprocessing.Process(target=draw_sst, args=(sel_year,sel_month,))    
    th_uv = multiprocessing.Process(target=draw_uv, args=(sel_year, sel_month,))    
    th_gh_500 = multiprocessing.Process(target=draw_gh_500hPa, args=(sel_year, sel_month,))    
    
    th_fre.start()
    th_sst.start()
    th_uv.start()
    th_gh_500.start()

    (th_uv.join())
    (th_sst.join())
    (th_gh_500.join())
    (th_fre.join())

    et2 = time.time()
    print(f"drawing plot takes {et2 - et1:.2}s")
    print("All done")



# f = Nio.open_file(filename, 'r')
# print((f.variables))
