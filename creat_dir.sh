#!/bin/bash
((0))&&{
1个routers
3个节点组成复制集作为配置服务器config server一主两从，不要仲裁节点
3个节点作为分片1:1主，1从，1仲裁
3个节点作为分片2:1主，1从，1仲裁
}


DATA_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/data/"
LOG_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/logs/"
CONF_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/conf/"
PID_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/pids/"
mkdir $DATA_DIR
mkdir $LOG_DIR
mkdir $CONF_DIR
mkdir $PIDS_DIR


# 创建两个分片各个节点的data、log、pid目录
for sh_name in sh1 sh2; do
	for rs_name in rs1 rs2 rs3; do
		mkdir -p $DATA_DIR$sh_name/$rs_name
	done
done
