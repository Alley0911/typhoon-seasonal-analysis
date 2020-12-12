import matplotlib.pyplot as plt
import numpy as np
import xarray as xr
import Nio
import os
import glob
import cartopy.crs as ccrs
import cartopy.feature as cfeature
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER
import matplotlib.ticker as mticker
from cartopy.io.shapereader import Reader


#------------------------------------------------------------------------------
# files_cli = sorted(glob.glob(os.path.join('/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cli', '*.grb')))
# file_cur = "/home/alley/work/Dong/mongo/seasonal_analysis/data/data/download_from_mongo/cur/gh_500_201911.grb"
# f_cli = xr.concat([xr.load_dataarray(file, engine="cfgrib") for file in files_cli], dim="time")
# c_cur = xr.load_dataarray(file_cur, engine="cfgrib")
# f_cli = xr.open_mfdataset(filenames_cli, engine="cfgrib", concat_dim=["time"])
#f_cur = Nio.open_file(filenames_cur)
# print(f_cli.dims)

#------------------------------------------------------------------------------
shp_path = '/home/alley/work/data/Cartopy_shapefiles/ne_50m_coastline.shp'
reader = Reader(shp_path)
proj = ccrs.PlateCarree(central_longitude=140)
coastlines = cfeature.ShapelyFeature(reader.geometries(), proj, edgecolor='k', facecolor='none')
fig = plt.figure(figsize=(4, 4), dpi=600)
ax = fig.subplots(1, 1, subplot_kw={'projection': proj})
ax.add_feature(coastlines, linewidth=0.7)
# ax.coastlines()
# ax.add_feature(cfeature.LAND)
# ax.add_feature(cfeature.COASTLINE, lw=0.3)
# ax.add_feature(cfeature.RIVERS, lw=0.3)
# ax.add_feature(cfeature.LAKES)
# ax.add_feature(cfeature.OCEAN)
extent = [100, 180, 0, 60]
ax.set_extent(extent)
gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=0.2, color='k', alpha=0.5, linestyle="--")
gl.xlabels_top = False
gl.ylabels_right = False
gl.xformatter = LONGITUDE_FORMATTER
gl.yformatter = LATITUDE_FORMATTER
gl.xlocator = mticker.FixedLocator(np.arange(extent[0], extent[1]+10, 10))
gl.ylocator = mticker.FixedLocator(np.arange(extent[2], extent[3]+20, 10))
gl.xlabel_style={'size': 2}
gl.ylabel_style={'size': 3.5}
plt.show()
