import re
import os
import time
import pandas as pd
import numpy as np
import linecache

# 这两个参数的默认可使列名对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

# 1. 创建df用来存放统计结果
years = range(1980, 2020, 1)
temp = np.zeros((12, len(years)), dtype=int)
months = range(1, 13, 1)
# print(temp)
res_out = pd.DataFrame(temp, months, columns=years)
print(res_out)

# 2. 读数据
res_in = pd.read_excel("/mnt/e/nmc/青年基金/data/各台风信息.xlsx")
clo = res_in.loc[:, ["生成的年份", "生成的月份"]]
# print(clo)
print(clo.index)


# # 3. 统计
# all_num = 0

for i in clo.index:
    month = clo.loc[i, "生成的月份"]
    year = clo.loc[i, "生成的年份"]
    # print(month)
    # print(year)
    # time.sleep(0.5)
    for i_month in months:
        for i_year in years:
            if month == i_month and year == i_year:
                res_out.loc[i_month, i_year] += 1
#                 # all_num += 1
#                 # res_out.loc["总数", "月频数"] = int(all_num)  # 按行增加+

# res_out = res_out.astype("int")  # 修改dataframe数据属性
res_out.loc[:, "均值"] = [0] * 12
res_out.loc[:, "最大值"] = [0] * 12
res_out.loc[:, "最小值"] = [0] * 12
res_out.loc[:, "总数"] = [0] * 12

# print(res_out.index)
for i in res_out.index:
    print(i)
    i -= 1
    res_out.loc[i + 1, "均值"] = round(np.mean(res_out.iloc[i, 0:len(years)]), 1)
    res_out.loc[i + 1, "最大值"] = (np.max(res_out.iloc[i, 0:len(years)]))
    res_out.loc[i + 1, "最小值"] = (np.min(res_out.iloc[i, 0:len(years)]))
    res_out.loc[i + 1, "总数"] = (np.sum(res_out.iloc[i, 0:len(years)]))

res_out.loc["总计"] = (res_out.apply(lambda x: x.sum())).astype("int")  # 
print(res_out)
# print(all_num)
# os.system("rm -rf /mnt/e/nmc/青年基金/data/台风月频数变化.xlsx")
# res_out.to_excel("/mnt/e/nmc/青年基金/data/台风月频数变化.xlsx")
os.system("rm -rf /mnt/e/nmc/青年基金/data/台风月频数变化.xlsx")
res_out.to_excel("/mnt/e/nmc/青年基金/data/台风月频数变化.xlsx")