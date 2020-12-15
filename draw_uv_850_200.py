import sys
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import Ngl,Nio
import os
import glob


def draw_uv(sel_year, sel_month):
	print("darwing wind plot for " + str(sel_month).zfill(2) + " " + str(sel_year))
	files_cli = sorted(glob.glob(os.path.join('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cli', 'uv*.grb')))
	f_cli = xr.open_mfdataset(files_cli, concat_dim="time", combine="nested", engine="cfgrib",parallel=True)
	u_cli_850 = f_cli["u"][:,0,:,:]
	v_cli_850 = f_cli["v"][:,0,:,:]
	u_cli_850 = u_cli_850.mean(dim="time")
	v_cli_850 = v_cli_850.mean(dim="time")
	u_cli_200 = f_cli["u"][:,1,:,:]
	v_cli_200 = f_cli["v"][:,1,:,:]
	u_cli_200 = u_cli_200.mean(dim="time")
	v_cli_200 = v_cli_200.mean(dim="time")


	file_cur = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cur/uv_850_200_" + str(sel_year) + str(sel_month).zfill(2) + ".grb"
	f_cur = xr.open_mfdataset(file_cur, engine="cfgrib", parallel=True)
	u_cur_850 = f_cur["u"][0,:,:]
	v_cur_850 = f_cur["v"][0,:,:]
	u_cur_200 = f_cur["u"][1,:,:]
	v_cur_200 = f_cur["v"][1,:,:]


	lat = f_cur["latitude"].values
	lon = f_cur["longitude"].values

	# u_ano_850 = u_cur_850 - u_cli_850
	# v_ano_850 = v_cur_850 - v_cli_850


	leftString = "850hPa wind"
	rightString = "m/s"
	wks_type = 'png'
	wks = Ngl.open_wks(wks_type, '/home/alley/work/Dong/mongo/seasonal_analysis/images/850_200_wind_' + str(sel_year) + str(sel_month) + '.png')

	res = Ngl.Resources()
	res.nglFrame = False
	res.nglDraw = False 
	res.mpLimitMode = "LatLon"
	res.mpMinLonF= 60
	res.mpMaxLonF = 180
	res.mpMinLatF = -10
	res.mpMaxLatF = 60

	res.mpPerimOn                 =  True                         #-- turn on map perimeter
	res.mpFillOn                  =  True                         #-- turn on map fill
	res.mpLandFillColor           =  "gray"                     #-- change land color to gray
	# resources.mpOceanFillColor       = -1     # Change oceans and inland
	# resources.mpInlandWaterFillColor = -1     # waters to transparent.
	res.mpOceanFillColor          =  "transparent"                #-- change color for oceans and inlandwater
	res.mpInlandWaterFillColor    =  "transparent"                #-- set ocean/inlandwater color to transparent
	res.mpGridMaskMode            = "MaskNotOcean"                #-- draw grid over ocean, not land
	res.vcMonoLineArrowColor      =  False                        #-- draw vectors in color
	res.vcMinFracLengthF          =   0.33                        #-- increase length of vectors
	res.vcMinMagnitudeF           =   0.001                       #-- increase length of vectors
	res.vcRefLengthF              =   0.045                       #-- set reference vector length
	res.vcRefMagnitudeF           =  10.0                         #-- set reference magnitude value
	res.vcLineArrowThicknessF     =   3                         #-- make vector lines thicker (default: 1.0)
	res.vcRefAnnoOn = False  # 不显示reference vector
	# res.vcLevelPalette            = "ncl_default"                 #-- choose color map

	res.pmLabelBarDisplayMode     = "Never"                      #-- turn on a labelbar
	res.lbOrientation             = "Horizontal"                  #-- labelbar orientation
	# res.lbLabelFontHeightF        =  0.008                        #-- labelbar label font size
	# res.lbBoxMinorExtentF         =  0.22                         #-- decrease height of labelbar boxes
	res.tiMainString = "850hPa wind field in " + str(sel_month).zfill(2) + " " + str(sel_year)

	# res.tiMainString = "850hPa wind"
	res.vfXArray                  =  lon[::15]                     #-- longitude values, subscript every 3rd value
	res.vfYArray                  =  lat[::15]                    #-- latitude values, subscript every 3rd value

	wind_850_cur = Ngl.vector_map(wks,u_cur_850[::15, ::15],v_cur_850[::15, ::15],res)           #-- draw a vector plot, subscript every 3rd value
	res.tiMainString = "850hPa wind field for climate state"
	wind_850_cli = Ngl.vector_map(wks,u_cli_850[::15, ::15],v_cli_850[::15, ::15],res)           #-- draw a vector plot, subscript every 3rd value
	res.tiMainString = "200hPa wind field in " + str(sel_month) + " " + str(sel_year)
	res.vfXArray                  =  lon[::15]                     #-- longitude values, subscript every 3rd value
	res.vfYArray                  =  lat[::15]                    #-- latitude values, subscript every 3rd value
	wind_200_cur = Ngl.vector_map(wks,u_cur_200[::15, ::15],v_cur_200[::15, ::15],res)           #-- draw a vector plot, subscript every 3rd value
	res.tiMainString = "200hPa wind field for climate state"
	wind_200_cli = Ngl.vector_map(wks,u_cli_200[::15, ::15],v_cli_200[::15, ::15],res)           #-- draw a vector plot, subscript every 3rd value


	panelres = Ngl.Resources()
	panelres.nglPanelLabelBar                 = True     # Turn on panel labelbar
	# panelres.nglPanelLabelBarLabelFontHeightF = 0.015    # Labelbar font height
	# panelres.nglPanelLabelBarHeightF          = 0.1750   # Height of labelbar
	# panelres.nglPanelLabelBarWidthF           = 0.700    # Width of labelbar
	# panelres.lbLabelFont                      = "helvetica-bold" # Labelbar font
	# panelres.nglPanelTop                      = 0.935
	Ngl.panel(wks,[wind_200_cli, wind_200_cur, wind_850_cli, wind_850_cur],[2,2],panelres)
	# panelres.nglPanelFigureStrings            = ["A","B","C","D","E","F"]
	# panelres.nglPanelFigureStringsJust        = "BottomRight"
	# vres = Ngl.Resources()
	# vres.nglFrame = False
	# vres.nglDraw = False 
	# vres.cnFillOn = True
	# vres.sfXArray = lon
	# vres.sfYArray = lat
	# vres.lbOrientation = "Horizontal"  # horizontal labelbar
	# vres.cnLinesOn = False
	# vres.cnLineLabelsOn = False
	# vres.cnLevelSelectionMode = "ExplicitLevels"
	# vres.cnFillPalette        = "BlueDarkRed18"
	# vres.cnLevels = np.arange(-5, 6, 1)
	# plot_cn = Ngl.contour(wks, h_ano, vres)

	# Ngl.overlay(plot_map, plot_cn)
	# Ngl.overlay(plot_map, plot2)
	# #
	# txres = Ngl.Resources()
	# txres.txFontHeightF = 0.024
	# #
	# Ngl.text_ndc(wks, leftString, 0.3, 0.83, txres) 
	# Ngl.text_ndc(wks, rightString, 0.85, 0.83, txres) 
	# #
	# Ngl.maximize_plot(wks, plot_map)
	# Ngl.draw(wind_850)
	# Ngl.frame(wks)
	Ngl.end()
	print("Finish darwing wind plot for " + str(sel_month).zfill(2) + " " + str(sel_year))



if __name__ == '__main__':
	sel_year = 2019
	sel_month = 11
	draw_uv(sel_year, sel_month)
