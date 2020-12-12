import sys
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import Ngl,Nio
import os
import glob
import netCDF4 as nc



files_cli = sorted(glob.glob(os.path.join('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cli', '*.grb')))
# f_cli = xr.concat([xr.load_dataarray(file, engine="cfgrib") for file in files_cli], dim="time")
# f_cli = nc.MFDataset(files_cli)
f_cli = xr.open_mfdataset(files_cli, concat_dim="time", combine="nested", engine="cfgrib")
# f_cli = xr.open_mfdataset(files_cli[0], engine="cfgrib")
h = f_cli["z"]
h = h.mean(dim="time")
h_cli = h/100
print(h.shape)

# print(h)


file_cur = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cur/gh_500_201911.grb"
f_cur = xr.open_mfdataset(file_cur, engine="cfgrib")
h_cur = f_cur["z"]/100
h_ano = h_cur - h_cli


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
res.cnLinesOn = False
res.cnLineLabelsOn = False
res.cnLevelSelectionMode = "ExplicitLevels"
res.cnFillPalette        = "BlueDarkRed18"
# res.cnLineLabelsOn = True
res.cnLevels = np.arange(-5, 6, 1)
#res.cnMonoLineThickness = False
#res.cnLineThicknesses = value
res.cnLineThicknessF=5
# res.cnInfoLabelOn=False
#res.cnLineColor="black"
plot = Ngl.contour_map(wks, h_ano, res)

cnres = Ngl.Resources()
cnres.nglFrame = False
cnres.cnFillOn = True
cnres.mpLimitMode = "LatLon"
cnres.mpMinLonF= 60
cnres.mpMaxLonF = 180
cnres.mpMinLatF = 0
cnres.mpMaxLatF = 60
cnres.sfXArray = lon
cnres.sfYArray = lat
cnres.cnLinesOn = False
cnres.cnLineLabelsOn = False 
cnres.cnLevelSelectionMode = "ExplicitLevels"
cnres.cnFillPalette        = "BlueDarkRed18"
cnres.cnLevels = np.arange(500, 600, 4)
cn#res.cnMonoLineThickness = False
cn#res.cnLineThicknesses = value
cnres.cnLineThicknessF=5
cn# res.cnInfoLabelOn=False
cn#res.cnLineColor="black"
plot1 = Ngl.contour_map(wks, h_cur, res)

Ngl.overlay(plot1, plot)

txres = Ngl.Resources()
txres.txFontHeightF = 0.024

Ngl.text_ndc(wks, leftString, 0.3, 0.78, txres) 
Ngl.text_ndc(wks, rightString, 0.9, 0.78, txres) 

Ngl.frame(wks)
Ngl.end()

# In[ ]:




