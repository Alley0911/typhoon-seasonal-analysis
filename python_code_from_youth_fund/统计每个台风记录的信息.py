import time
import re
import pandas as pd
import numpy as np
import linecache
import os



# 这两个参数的默认可使列名对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
# 显示所有列
pd.set_option('display.max_columns', None)
# 显示所有行
pd.set_option('display.max_rows', None)

# 1. 生成一个DataFrame数据用于存放结果
temp = np.zeros((1, 1), dtype=int)
# print(temp)
years = range(1, 2, 1)
# print(years)
res = pd.DataFrame(temp, index=years, columns=["名字"])
res["编号"] = temp
res["首行数"] = temp
res["最后的行数"] = temp
res["生成的年份"] = temp
res["最后的年份"] = temp
res["生成的月份"] = temp
res["最后的月份"] = temp
res["生成的时间"] = temp
res["最后的时间"] = temp
# res.loc[1, "名字"] = 'alley'
# res.loc[2, "名字"] = 'alley'
# print(res)

# 2. 统计 713(不包括副中心和非编号的记录)
file_path = "/mnt/e/nmc/青年基金/data/1980-2019_TS之上且无转性的记录.txt"
with open(file_path, "r") as f_in:
    num_ty = 1
    tempp = 1
    for num, line in enumerate(f_in, start=1):  # 得到行数和每行的内容，start=1表示index从1开始不是从0
        title = linecache.getline(file_path, num)  # 得到第几行的内容，第几行就是第几行首行不是0
        col = re.split(r" +", title)
        if len(col) > 7 and \
        col[4] != "0000" and \
        col[7] != "(nameless)" and \
        col[7][-1] not in ["1", "2"]:
            col_title = col
            name = col_title[7]
            id_num = col_title[4]
            res.loc[num_ty, "名字"] = name
            res.loc[num_ty, "编号"] = id_num

            num_record_begin = num + 1  # 表示头记录后面的第一行记录的行数即台风开始的行数
            # print(num_record_begin)
            # time.sleep(0.5)
            record_begin = linecache.getline(file_path, num_record_begin)
            col_record_begin = re.split(r" +", record_begin)
            res.loc[num_ty, "生成的时间"] = col_record_begin[0]
            res.loc[num_ty, "生成的年份"] = col_record_begin[0][0:4]
            res.loc[num_ty, "生成的月份"] = col_record_begin[0][4:6]
            res.loc[num_ty, "首行数"] = num_record_begin

            num_record = num_record_begin  # 表示头记录后面的第一行，后续会通过累加表示后面的行
            record = linecache.getline(file_path, num_record)
            col_record = re.split(r" +", record)
            grade = int(col_record[1])
            # print(grade)
            while 1 < len(col_record) <= 7 and grade >= 2:  # get每个台风最后的时间和行数
                res.loc[num_ty, "最后的时间"] = col_record[0]
                res.loc[num_ty, "最后的年份"] = col_record[0][0:4]
                res.loc[num_ty, "最后的月份"] = col_record[0][4:6]
                res.loc[num_ty, "最后的行数"] = num_record
                num_record += 1
                record = linecache.getline(file_path, num_record)
                print(col_record)
                grade = int(col_record[1])
                col_record = re.split(r" +", record)
                # print(num_record, grade, record)
                # time.sleep(0.5)
            num_ty += 1  # 记录台风的个数
            print(num_ty)

# print(res)
os.system("rm -rf /mnt/e/nmc/青年基金/data/各台风信息.xlsx")
res.to_excel("/mnt/e/nmc/青年基金/data/各台风信息.xlsx")


