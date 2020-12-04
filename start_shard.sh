#!/bin/bash

CONF_DIR="/home/alley/work/Dong/mongo/seasonal_analysis/conf/"

for sh_name in sh1 sh2 cfs; do
	for rs_name in rs1 rs2 rs3;	do
		args=$CONF_DIR${sh_name}_${rs_name}.conf
		echo $args
		./start_one_mongo_with_expect.sh $args
	done
done
