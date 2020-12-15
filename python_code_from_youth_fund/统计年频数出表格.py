import re
import os
import time
import pandas as pd
import numpy as np
import linecache

# 这两个参数的默认可使列名对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)

# 1. 创建df用来存放统计结果
temp = np.zeros((40,1), dtype=int)
# print(temp)
res_out = pd.DataFrame(temp, index=range(1980,2020,1), columns=["年频数"])
print(res_out)

# 2. 读数据
res_in = pd.read_excel("/mnt/e/nmc/青年基金/data/各台风信息.xlsx")
year_clo = res_in.loc[:, ["生成的年份", "最后的年份"]]
# print(year_clo)
# print(year_clo.index)


# 3. 统计
all_num = 0
years = range(1980, 2020, 1)
for i in year_clo.index:
    year_begin = year_clo.loc[i, "生成的年份"]
    year_end = year_clo.loc[i, "最后的年份"]
    # if not year_begin==year_end:
    #     print(year_begin,year_end)
    for i in years:
        if year_begin == i:
            temp = res_out.loc[i, "年频数"]
            # print(temp)
            temp += 1 
            res_out.loc[i, "年频数"] = int(temp)
            all_num += 1
    res_out.loc["总数", "年频数"] = int(all_num)  # 按行增加+
res_out = res_out.astype("int")  # 修改dataframe数据属性
# print(res_out)
# print(all_num)
os.system("rm -rf /mnt/e/nmc/青年基金/data/台风年频数变化.xlsx")
res_out.to_excel("/mnt/e/nmc/青年基金/data/台风年频数变化.xlsx")