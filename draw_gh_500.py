import sys
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import Ngl,Nio
import os
import glob


files_cli = sorted(glob.glob(os.path.join('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cli', '*.grb')))
f_cli = xr.open_mfdataset(files_cli, concat_dim="time", combine="nested", engine="cfgrib")
h = f_cli["z"]
h = h.mean(dim="time")
h_cli = h/98
 

file_cur = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cur/gh_500_201911.grb"
f_cur = xr.open_mfdataset(file_cur, engine="cfgrib")
h_cur = f_cur["z"]/98
h_ano = h_cur - h_cli


lat = f_cli["latitude"].values
lon = f_cli["longitude"].values
leftString = "500hPa Height & Anomaly"
rightString = "dagpm"

wks_type = 'png'
wks = Ngl.open_wks(wks_type, '/home/alley/work/Dong/mongo/seasonal_analysis/images/gh_500hPa_cli.png')

res = Ngl.Resources()
res.nglFrame = False
res.nglDraw = False 
res.mpLimitMode = "LatLon"
res.mpMinLonF= 60
res.mpMaxLonF = 180
res.mpMinLatF = 0
res.mpMaxLatF = 60
plot_map = Ngl.map(wks, res)

fres = Ngl.Resources()
fres.nglFrame = False
fres.nglDraw = False 
fres.cnFillOn = True
fres.sfXArray = lon
fres.sfYArray = lat
fres.lbOrientation = "Horizontal"  # horizontal labelbar
fres.cnLinesOn = False
fres.cnLineLabelsOn = False
fres.cnLevelSelectionMode = "ExplicitLevels"
fres.cnFillPalette        = "BlueDarkRed18"
fres.cnLevels = np.arange(-5, 6, 1)
plot_cn = Ngl.contour(wks, h_ano, fres)



cnres = Ngl.Resources()
cnres.nglDraw = False
cnres.nglFrame = False
cnres.cnFillOn = False 
cnres.cnLinesOn = True
cnres.cnLineLabelsOn = True 
cnres.cnInfoLabelOn = False
cnres.sfXArray = lon
cnres.sfYArray = lat
cnres.cnLevelSelectionMode = "ExplicitLevels"
cnres.cnLevels = np.arange(500, 600, 4)
cnres.cnLineColor="black"
cnres.cnLineThicknessF=5
plot2 = Ngl.contour(wks, h_cur, cnres)

Ngl.overlay(plot_map, plot_cn)
Ngl.overlay(plot_map, plot2)
#
txres = Ngl.Resources()
txres.txFontHeightF = 0.024
#
Ngl.text_ndc(wks, leftString, 0.3, 0.83, txres) 
Ngl.text_ndc(wks, rightString, 0.85, 0.83, txres) 
#
Ngl.maximize_plot(wks, plot_map)
Ngl.draw(plot_map)
Ngl.frame(wks)
Ngl.end()
#
## In[ ]:
#
#
#
#
##res.cnLineThicknesses = value
