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
mon = list(range(7,10))
year = list(range(1980,2020))
df_tc_5_11 = df_tc_mon.loc[mon,year]
sum_5_11 = df_tc_5_11.sum(axis=0)
mean_5_11 = np.mean(sum_5_11)
std_5_11 = np.std(sum_5_11)
# print(df_tc_5_11)
print(sum_5_11)
# print(mean_5_11)
scale_5_11 = (sum_5_11 - mean_5_11)/std_5_11
# print(scale_5_11.index)
more = []
less = []
for value,year in zip(scale_5_11,scale_5_11.index):
    if value >= 1:
        more.append(year)
        print("more year:{0},value:{1}".format(year,value))
    if value <= -1:
        less.append(year)
        print("less year:{0},value:{1}".format(year,value))
print(more)
print(less)

df_MEI = pd.read_excel("E:/nmc/青年基金/data/MEI.xlsx",header=0,index_col=0)
# print(df_MEI)
mean_MEI = df_MEI.mean(axis=1)
# print(mean_MEI)
more_num = 0
less_num = 0
print("more year La Nina百分率")
for i in more:
    if mean_MEI[i] < 0:
        more_num += 1
print(more_num/len(more))
print("less year El Nino百分率")
for i in less:
    if mean_MEI[i] > 0:
        less_num += 1
print(less_num/len(less))
