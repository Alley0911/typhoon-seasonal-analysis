import sys
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import Ngl,Nio
import os
import glob


def draw_gh_500hPa(sel_year, sel_month):
	print("darwing 500hPa gh plot for " + str(sel_month).zfill(2) + " " + str(sel_year))
	files_cli = sorted(glob.glob(os.path.join('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cli/', 'gh_500_*.grb')))
	f_cli = xr.open_mfdataset(files_cli, concat_dim="time", combine="nested", engine="cfgrib",parallel=True)
	h = f_cli["z"]
	h = h.mean(dim="time")
	h_cli = h/98

	lat = f_cli["latitude"].values
	lon = f_cli["longitude"].values




	file_cur = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cur/gh_500_" + str(sel_year) + str(sel_month).zfill(2) + ".grb"
	# print(file_cur)
	f_cur = xr.open_mfdataset(file_cur, engine="cfgrib", parallel=True)
	h_cur = f_cur["z"]/98


	h_ano = h_cur - h_cli


	leftString = "500hPa Height & Anomaly for " + str(sel_month) + str(sel_year)
	rightString = "dagpm"
	wks_type = 'png'
	wks = Ngl.open_wks(wks_type, '/home/alley/work/Dong/mongo/seasonal_analysis/images/gh_500hPa_' + str(sel_year) + str(sel_month).zfill(2) + '.png')

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

	print("Finish darwing 500hPa gh plot plot for " + str(sel_month).zfill(2) + " " + str(sel_year))

if __name__ == '__main__':
	sel_year = 1998
	sel_month = 7
	draw_gh_500hPa(sel_year, sel_month)
