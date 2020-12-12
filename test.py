#!/usr/bin/env python
# coding: utf-8

# In[1]:


import sys
sys.path.append("/home/alley/anaconda3/envs/ncl_to_python/lib/python3.8/site-packages")
sys.path.append("/home/alley/anaconda3/envs/ncl_to_python/lib/python3.8/site-packages/PyNIO")


# In[2]:


import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import Ngl,Nio
import os
import glob
import netCDF4 as nc


# In[18]:


files_cli = sorted(glob.glob(os.path.join('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cli', '*.grb')))
# f_cli = xr.concat([xr.load_dataarray(file, engine="cfgrib") for file in files_cli], dim="time")
# f_cli = nc.MFDataset(files_cli)
f_cli = xr.open_mfdataset(files_cli, concat_dim="time", combine="nested", engine="cfgrib")
# f_cli = xr.open_mfdataset(files_cli[0], engine="cfgrib")
h = f_cli["z"]
h = h.mean(dim="time")
h = h/100
print(h.shape)

# In[19]:


lat = f_cli["latitude"].values
lon = f_cli["longitude"].values
leftString = "500hPa Height & Anomaly"
rightString = "dagpm"

wks_type = 'png'
wks = Ngl.open_wks(wks_type, '/home/alley/work/Dong/mongo/seasonal_analysis/images/gh_500hPa_cli.png')

res = Ngl.Resources()
res.nglFrame = False
res.cnFillOn = True
res.mpLimitMode = "LatLon"
res.mpMinLonF= 60
res.mpMaxLonF = 180
res.mpMinLatF = 0
res.mpMaxLatF = 60
res.sfXArray = lon
res.sfYArray = lat
res.cnLevelSelectionMode = "ExplicitLevels"
# res.cnLineLabelsOn = True
res.cnLevels = np.arange(492, 600, 4)
#res.cnMonoLineThickness = False
#res.cnLineThicknesses = value
res.cnLineThicknessF=5
# res.cnInfoLabelOn=False
res.cnLineColor="black"
plot = Ngl.contour_map(wks, h, res)

txres = Ngl.Resources()
txres.txFontHeightF = 0.024

Ngl.text_ndc(wks, leftString, 0.3, 0.78, txres) 
Ngl.text_ndc(wks, rightString, 0.9, 0.78, txres) 

Ngl.frame(wks)
Ngl.end()
print("ok")


# In[ ]:


#file_cur = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cur/gh_500_201911.grb"

