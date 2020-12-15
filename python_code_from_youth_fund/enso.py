import pandas as pd
import numpy as np


el = []
la = []
data = np.ones((40,12),dtype=float)
df_ONI = pd.read_excel('E:/nmc/青年基金/data/ONI.xls',index_col=0)
df_80_19 = pd.DataFrame(data,index=range(1980,2020),columns=range(1,13))
for i in range(1980,2020):
	temp_list=np.array((list(df_ONI.loc[i,:])))
	if np.sum(temp_list>=0.5)>=5:
		el.append(i)
	if np.sum(temp_list<=-0.5)>=5:
		la.append(i)
print("El Nino")
print(el)
print("La Nina")
print(la)
for i in el:
	if i in la:
		print(i)