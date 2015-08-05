__author__ = 'woo409'

import xray

array = xray.open_dataset('/home/woo409/LS5TM_2011_-37_147.nc')
lat_res = array.attrs['geospatial_lat_resolution']
lon_res = array.attrs['geospatial_lon_resolution']
lat_max = array.attrs['geospatial_lat_max']
lon_max = array.attrs['geospatial_lon_max']

lon_min = lon_max-(128.0*lon_res)
lat_min = lat_max+(128.0*lat_res)

subset1 = array.isel(latitude=slice(3750,3999), longitude=slice(0,249))
subset2 = array.sel(latitude=slice(lat_max, lat_min), longitude=slice(lon_min, lon_max))

#subset.attrs['geospatial_lot_max'] = #TODO: insert minimum here
#subset.to_netcdf('saved_on_disk.nc')