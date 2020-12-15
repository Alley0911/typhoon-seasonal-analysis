import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import  MultipleLocator
from matplotlib.ticker import  FormatStrFormatter


# 这两个参数的默认可使列名对齐
pd.set_option('display.unicode.ambiguous_as_wide', True)
pd.set_option('display.unicode.east_asian_width', True)
def draw_frequency(sel_year):
	print("darwing frequency plot for " + str(sel_year))
	##########################################################################
	# 1. 读数据
	##########################################################################
	begin1 = 1990
	end1 = 2019
	sel_year = sel_year 
	num1 = end1 - begin1 + 1
	res_in = pd.read_excel("/home/alley/work/Dong/mongo/seasonal_analysis/ty_data/台风月频数变化.xlsx", index_col=0)  # 将表格文件第一列作为res_in的index
	# print(res_in)
	# print(res_in.index)
	years = range(begin1, end1 + 1, 1)
	x1 = years
	y1 = res_in.loc["总计", years]
	# print(x)
	# print(y)
	y1_avg = round(np.mean(y1), 1)
	y11 = [np.mean(y1)] * len(years)
	# print("一共%d年,平均年频数为%.1f" % (num1, y1_avg))

	months = range(1, 13)
	x2 = months
	df_month = res_in.loc[months, [sel_year,"均值", "最大值", "最小值"]]
	# df_month.columns = ["mean", "max", "min"]
	# print(df_month)

	# y2 = list(df_month.values)
	# print(y2)

	#########################################################################
	# 1. 画图
	#########################################################################
	plt.figure(figsize=(10,7))
	# 1.1 画年变化在上
	ax1 = plt.subplot(211)
	ax1.set_xlim((1989, 2021))
	ax1.set_ylim((10, 40))

	# 主副刻度设置
	# 将x主刻度标签设置为5的倍数(也即以 5为主刻度单位其余可类推)
	xmajorLocator = MultipleLocator(5)
	# 设置x轴标签文本的格式
	xmajorFormatter = FormatStrFormatter('%d') 
	# 将x轴次刻度标签设置为1的倍数
	xminorLocator = MultipleLocator(1)
	# 设置主刻度标签的位置,标签文本的格式
	ax1.xaxis.set_major_locator(xmajorLocator)
	ax1.xaxis.set_major_formatter(xmajorFormatter)
	# 显示次刻度标签的位置,没有标签文本
	ax1.xaxis.set_minor_locator(xminorLocator)


	# ax1.set_title("年频数")  # 不能出现中文
	ax1.set_xlabel('Year')
	ax1.set_ylabel('Frequency')
	# ax1.figure(num=1,figsize=(15,5))
	ax1.plot(x1, y1, color="r", linewidth=2.0)
	ax1.plot(x1, y11, color="blue", linewidth=2.0, linestyle="--", label="mean")
	ax1.scatter(x1, y1, s=50, c="r", alpha=1,)
	ax1.text(2018, y1_avg-3, y1_avg, c="blue")
	ax1.legend()

	#########################################################################

	ax2 = plt.subplot(212)
	ax2.set_xlim((0, 13))
	ax2.set_ylim((0, 10))
	ax2.set_xlabel('Month')
	ax2.set_ylabel('Frequency')
	ax2.set_xticks(range(1, 13))
	ax2.set_yticks(range(0, 11))
	x2 = months
	y21 = df_month["均值"]
	y22 = df_month["最大值"]
	y23 = df_month["最小值"]
	y24 = df_month[sel_year]
	# print(y24)
	ax2.plot(x2, y21, color="k", label="mean")
	ax2.scatter(x2, y21, color="k")
	ax2.plot(x2, y22, color="b", label="max")
	ax2.scatter(x2, y22, color="b")
	ax2.plot(x2, y23, color="g", label="min")
	ax2.scatter(x2, y23, color="g")
	ax2.plot(x2, y24, color="r", label=str(sel_year))
	ax2.scatter(x2, y24, color="r")
	# df_month.plot(x="index", y=["min"], ax=ax2, color="b")
	# df_month.plot.scatter(x="index", y=["min"], color="b", ax=ax2)
	# df_month.plot(x="index", y=["max"], ax=ax2, color="g")
	# df_month.plot.scatter(x="index", y=["max"], color="g", ax=ax2)
	# df_month.plot.scatter(x="index", y=["min"], ax=ax2)
	# df_month.plot.scatter(x="index", y=["max"], ax=ax2)
	ax2.legend()  # 加上这一句 label 才能显示
	plt.grid(axis='y')  # 添加网格
	# plt.show()
	plt.savefig("/home/alley/work/Dong/mongo/seasonal_analysis/images/frequency_" + str(sel_year) + ".png", dpi=300, bbox_inches='tight')
	print("Finish darwing frequency plot for " + str(sel_year))
if __name__ == '__main__':
	draw_frequency(2019)