import pandas as pd
import numpy as np
import matplotlib.pyplot as py
import datetime
from scipy.stats import pearsonr

def scale1(x):
    return (x - np.mean(x))/np.std(x)
def scale2(x):
    return (x - np.min(x))/(np.max(x)-np.min(x))


df_tc_mon = pd.read_excel("E:/nmc/青年基金/data/台风月频数变化.xlsx",header=0,index_col=0)
print(df_tc_mon)
year = range(1980,2020)
start_mon = [5,6,7]
end_mon = [10,11]
mon = []  # 月份的分类
tc = []  # 不同月份的tc频数序列
tc_tmp = []
time_tmp=[]
time=[]  # 不同个月的时间序列
for i in start_mon:
    for j in end_mon:
        mon.append(np.array(range(i,j+1)))

for mon_cur in mon:
    # print(mon_cur)
    for k in year:
        for j in (mon_cur):
            tmp = df_tc_mon.loc[j,k]
            tc_tmp.append(tmp)
    tc.append(np.array(tc_tmp))
    for y in year:
        for m in mon_cur:
            tmp = datetime.datetime(y,m,1)
            time_tmp.append(tmp)
    time.append(np.array(time_tmp))
    tc_tmp = []
    time_tmp = []

sh = pd.read_excel("E:/nmc/青年基金/data/副高指数.xlsx",header=0,index_col=0).loc[1980:2019]
sh_index = sh.columns[1:]
new_index = []
for i in year:
    for m in range(1,13):
        new_index.append(str(i)+'_'+str(m))
sh.index=new_index
print(sh)
area_index=[]
area_index_tmp=[]
intensity_index=[]
intensity_index_tmp=[]
lat_tmp = []
lat = []
lon_tmp = []
lon = []
for mon_cur in mon:
    for k in year:
        for m in mon_cur:
            # print(m)
            row = str(k) + "_" + str(m)
            tmp = sh.loc[row,'面积指数']
            area_index_tmp.append(tmp)
            tmp = sh.loc[row,'强度指数']
            intensity_index_tmp.append(tmp)
            tmp = sh.loc[row,'脊线纬度']
            lat_tmp.append(tmp)
            tmp = sh.loc[row,'西伸脊点']
            lon_tmp.append(tmp)
    area_index.append(np.array(area_index_tmp))
    intensity_index.append(np.array(intensity_index_tmp))
    lat.append(np.array(lat_tmp))
    lon.append(np.array(lon_tmp))
    area_index_tmp = []
    intensity_index_tmp = []
    lat_tmp = []
    lon_tmp = []

relation = []
relation_tmp = []
p_value = []
p_value_tmp = []
for index_cur in [area_index,intensity_index,lat,lon]:
    for id_mon in range(len(mon)):
        r,p = pearsonr(scale2(index_cur[id_mon]),scale2(tc[id_mon]))
        relation_tmp.append(r)
        p_value_tmp.append(p)
    p_value.append(np.array(p_value_tmp))
    relation.append(np.array(relation_tmp))
    relation_tmp = []
    p_value_tmp = []
for i in range(len(sh_index)):
    print(sh_index[i])
    print(relation[i])
    print(p_value[i])
print(mon)
# 脊线纬度与tc生成有显著正相关，对应的月份为5，6，7，8，9，10，11月份，在99%的显著性水平上相关

lat_2019_11 = sh.loc["2019_7",'脊线纬度']
lat_cli = 0.0
for y in range(1981,2011):
    m = 11
    row = str(y) + "_" + str(m)
    lat_cli = lat_cli + sh.loc[row,'脊线纬度']
lat_cli = lat_cli / 30
print(lat_cli)  # 气候态11月份脊线纬度
print(lat_2019_11)  # 2019年11月份脊线纬度
