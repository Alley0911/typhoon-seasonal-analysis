import re
import os
'''
删除强度低于TS、转性的路径记录;
删除3小时间隔的记录，只保留00，06，12，18时刻的路径记录;
删除nameless的头记录;
保留副中心的头记录和路径记录。
'''

os.system("rm -rf /mnt/e/nmc/青年基金/data/1990-2019_无无效记录.txt")
file_names = os.listdir("/mnt/e/nmc/青年基金/data/ori_data")
sub_num = ["1", "2"]  # 用来判断名字是否为副中心，因为副中心的名字的最后一位为数字
# print(file_names)
for file_name in file_names:
    print(file_name)
    with open("/mnt/e/nmc/青年基金/data/ori_data/" + file_name, "r") as f_in:
        for line in f_in:
            col = re.split(r" +", line)

            if len(col) > 7:  # 避免操作路径
                if col[7] != "(nameless)" and col[7][-1] not in sub_num:  # 判断头文件是否是nameless和副中心
                    with open("/mnt/e/nmc/青年基金/data/1990-2019_无无效记录.txt", "a+") as f_out:
                        f_out.write(line)

            if len(col) > 2:  # 避免操作空行
                if int(col[1]) >= 2 and int(col[1]) < 9:  # 判断记录是否强于TS
                    time = [0, 6, 2, 8]
                    if int(col[0][-1]) in time:  # 判断是否时6小时间隔的记录
                        with open("/mnt/e/nmc/青年基金/data/1990-2019_无无效记录.txt", "a+") as f_out:
                            f_out.write(line)



