import sys
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import Ngl,Nio
import os
import glob
import time


def draw_sst(sel_year, sel_month):
    st = time.time()
    np.seterr(divide='ignore', invalid='ignore')
    print("darwing sst plot for " + str(sel_month).zfill(2) + " " + str(sel_year))
    files_cli = sorted(glob.glob(os.path.join('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cli', 'sst_*.grb')))
    f_cli = xr.open_mfdataset(files_cli, concat_dim="time", combine="nested", engine="cfgrib",parallel=True)
    h_cli = f_cli["sst"]
    h_cli_ori = h_cli.mean(dim="time").values


    file_cur = "/home/alley/new_disk/data/sst_" + str(sel_year) + str(sel_month).zfill(2) + ".grb"
    f_cur = xr.open_mfdataset(file_cur, engine="cfgrib", parallel=True)
    h_cur_ori = f_cur["sst"]
    h_cur = (h_cur_ori.values - 273.15)
    h_cur = np.nan_to_num(h_cur, nan=-999)


    lat = f_cur["latitude"].values
    lon = f_cur["longitude"].values


    h_ano = h_cur_ori - h_cli_ori
    h_ano = np.nan_to_num(h_ano.values, nan=-999)
    # print(h_ano)

    et1= time.time()
    # print(et1 - st)
    # leftString = "SST in " + str(sel_month) + str(sel_year)
    # rightString = "~S~o~N~C"
    wks_type = 'png'
    wks = Ngl.open_wks(wks_type, '/home/alley/work/Dong/mongo/seasonal_analysis/images/sst_' + str(sel_year) + str(sel_month).zfill(2) + '.png')

    res = Ngl.Resources()
    res.nglFrame = False
    res.nglDraw = False 
    res.mpLimitMode = "LatLon"
    # res.mpFillOn                  =  True                         #-- turn on map fill
    # res.mpLandFillColor           =  "gray"                     #-- change land color to gray
    # res.mpMinLonF= 50
    # res.mpMaxLonF = 280
    res.mpMinLatF = -45
    res.mpMaxLatF = 45
    res.cnFillOn = True
    res.mpCenterLonF = 120
    res.sfMissingValueV             = -999
    res.sfXArray = lon
    res.sfYArray = lat
    res.lbOrientation = "Horizontal"  # horizontal labelbar
    res.cnLinesOn = False
    res.tiMainFontHeightF = 0.015
    res.cnLineLabelsOn = False
    res.cnFillDrawOrder = "Predraw"
    res.cnFillPalette        = "BlAqGrYeOrRe"
    res.pmLabelBarDisplayMode     = "Always"                      #-- turn on a labelbar
    res.tiMainString = "SST in " + str(sel_month).zfill(2) + " " + str(sel_year) + " (degC)"
    res.cnLevelSelectionMode = "ExplicitLevels"
    res.cnLevels = np.arange(20, 35, 1)
    plot_cur = Ngl.contour_map(wks, h_cur, res)


    res.cnLevelSelectionMode = "ExplicitLevels"
    res.tiMainString = "SST anomaly in " + str(sel_month).zfill(2) + " " + str(sel_year) + " (degC)"
    res.cnFillPalette  = "GMT_polar"
    res.cnLevels = np.arange(-3, 4, 1)
    res.pmLabelBarHeightF = 0.3
    plot_ano = Ngl.contour_map(wks, h_ano, res)
    Ngl.panel(wks,[plot_cur, plot_ano], [2, 1], False)
    Ngl.end()
    et2 = time.time()
    # print(et2 - et1)
    print("Finish darwing sst plot for " + str(sel_month).zfill(2) + " " + str(sel_year))

if __name__ == '__main__':
    sel_year = 2019
    sel_month = 11
    draw_sst(sel_year, sel_month)
