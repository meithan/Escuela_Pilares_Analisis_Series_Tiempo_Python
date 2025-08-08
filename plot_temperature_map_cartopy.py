# Plots the temperature anomalies for the Berkeley Earth dataset

import datetime as dtm
import locale
import os
import sys

import cartopy
import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from mpl_toolkits.axes_grid1 import make_axes_locatable
import matplotlib.colors as mcolors
from matplotlib.colors import LinearSegmentedColormap
import numpy as np

from netCDF4 import Dataset
import numpy as np

PlateCarree = ccrs.PlateCarree()
Geodetic = ccrs.Geodetic()
Robinson = ccrs.Robinson()
Orthographic = ccrs.Orthographic(central_longitude=-90)
GoodeHomolosine = ccrs.InterruptedGoodeHomolosine()
Mollweide = ccrs.Mollweide()

# ==============================================================================

# Download from: https://berkeley-earth-temperature.s3.us-west-1.amazonaws.com/Global/Gridded/Land_and_Ocean_EqualArea.nc
data_fpath = "Land_and_Ocean_EqualArea.nc"

# ----------------------------------------
# Read NetCDF data

data = Dataset(data_fpath)
print(data)

print("Data model: ", data.data_model)
print("File format: ", data.file_format)
print("Disk format: ", data.disk_format)
print("\nGroups:")
for group in data.groups:
  print(group)
print("\nVariables:")
for var in data.variables:
  print(var)
print("\nDimensions:")
for dimension in data.dimensions:
  print(dimension)
print()

times = data.variables["time"][:]
num_times = times.shape[0]
print(f"{num_times} time values from {times[0]:.2f} to {times[-1]:.2f}")

temperature = data.variables["temperature"]
num_cells = temperature.shape[1]
print("{:,} grid cells".format(num_cells))
# print(temperature.shape)

lats = data.variables["latitude"][:]
lons = data.variables["longitude"][:]
# print(lats.shape, lons.shape)

month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# ----------------------------------------

map_proj = Mollweide
# map_proj.transform_points(ccrs.Geodetic(), lons, lats)

fig = plt.figure(figsize=(15, 8))
ax = plt.axes(projection=map_proj)

#for country in plot_countries:
#ax.add_geometries(country.geometry, ccrs.PlateCarree(), edgecolor='black', facecolor="none", linewidth=1)

# ax.set_extent([-180, 180, -80, 80], Geodetic)
ax.coastlines(color="gray", linewidth=1)
gl = ax.gridlines(draw_labels=True, linestyle=":")
gl.xlabel_style = {"color": "0.5"}
gl.ylabel_style = {"color": "0.5"}
gl.xlines = True
gl.ylines = True

# Plot temperature field
cmap = LinearSegmentedColormap.from_list('custom', ['blue', "white", 'red'], N=256)
cmap = "seismic"
size = 20
vmin = -4
vmax = 4
sc = plt.scatter(lons, lats, s=size, c=temperature[-1], cmap=cmap, vmin=vmin, vmax=vmax, ec="none", alpha=0.7, transform=Geodetic)

text = f"Temperature anomalies for {times[-1]:.2f} (1951-1980 baseline) | Data from Berkeley Earth"
plt.suptitle(text, fontsize=14)

# Plot colorbar
divider = make_axes_locatable(ax)
cax = divider.new_horizontal(size="2%", pad=0.6, axes_class=plt.Axes)
fig.add_axes(cax)
cb = plt.colorbar(sc, cax=cax)
# cb = plt.colorbar(sc)
cb.ax.set_title("Anomaly (°C)")
fmter = lambda value, pos: "0" if value == 0 else f"{value:+.0f}"
cb.ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmter))

plt.tight_layout()
plt.show()



