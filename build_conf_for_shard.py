import sys
import os


DATA_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/data/"
LOG_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/logs/"
CONF_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/conf/"
PID_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/pids/"


# 用于编辑.conf文件
dbpath = "/home/alley/work/Dong/mongo/seasonal_analysis/data/"
logpath = "/home/alley/work/Dong/mongo/seasonal_analysis/logs/"
pidfilepath = "/home/alley/work/Dong/mongo/seasonal_analysis/pids/"
port = 27017
replSet = 'sh1'
shardsvr = 'true'  # 用于确认是分片的
configsvr = "true"
# 追加日志而不是重新创建
# oplog日志的文件大小，副本集通过该日志同步主节点的数据库操作
# 每个数据库放在单独的文件夹下
others = '''logappend=true 
bind_ip_all=true
fork=true
oplogSize=10000
directoryperdb=true'''

sh_name = ['sh1', 'sh2', "cfs"]
rs_name = ['rs1', 'rs2', 'rs3'] # 一主一从一仲裁，仲裁英文arbiter,如果是配置服务器，则不需要有仲裁节点
# sh1 port:27017,27018,27019
# sh2 port:27117,27118,27119
# cfs port:27217,27218,27219
for sh_name_ in sh_name:
	for rs_name_ in rs_name:
		with open(CONF_DIR + sh_name_ + "_" + rs_name_ + ".conf", 'w') as fout:
			fout.write("dbpath=" + dbpath + sh_name_ + "/" + rs_name_ + "/" + "\n")
			fout.write("logpath=" + logpath + sh_name_ + "_" + rs_name_ + ".log\n")
			fout.write("pidfilepath=" + pidfilepath + sh_name_ + "_" + rs_name_ + ".pid\n")
			fout.write("port=" + str(port) + "\n")
			fout.write("replSet=" + sh_name_ + "\n")
			if sh_name_ == "cfs":
				fout.write("configsvr=" + configsvr + "\n")
			else:
				fout.write("shardsvr=" + shardsvr + "\n")
			fout.write(others)
		port += 1
	port -= 3
	port += 100