import xarray as xr
import matplotlib.pyplot as plt
import easygems.healpix as egh
import cartopy.crs as ccrs

# define paths
datapath = '/scratch/nf33/Healpix_data/'
model = 'UM'
zoom = 'z2'
fpath = f'{datapath}{model}/data.healpix.PT1H.{zoom}.zarr'

# open the zarr file
ds = xr.open_zarr(fpath)

# what variables are there in the dataset?
for key, longname in ds.data_vars.items():
    print(f'{key}: {longname.long_name}')

'''
clivi:  atmosphere_mass_content_of_cloud_ice
clt:    cloud_area_fraction
clwvi:  atmosphere_mass_content_of_cloud_condensed_water
hflsd:  surface_downward_latent_heat_flux
hfssd:  surface_downward_sensible_heat_flux
huss:   specific_humidity
pr:     precipitation_flux
prs:    solid_precipitation_flux
prw:    atmosphere_mass_content_of_water_vapor
ps:     surface_air_pressure
psl:    air_pressure_at_mean_sea_level
rlds:   surface_downwelling_longwave_flux_in_air
rldscs: surface_downwelling_longwave_flux_in_air_clear_sky
rlut:   toa_outgoing_longwave_flux
rlutcs: toa_outgoing_longwave_flux_clear_sky
rsds:   surface_downwelling_shortwave_flux_in_air
rsdscs: surface_downwelling_shortwave_flux_in_air_clear_sky
rsdt:   toa_incoming_shortwave_flux
rsut:   toa_outgoing_shortwave_flux
rsutcs: toa_outgoing_shortwave_flux_clear_sky
tas:    air_temperature
ts:     surface_temperature
uas:    eastward_wind
vas:    northward_wind
'''

# choose a variable to plot
da = ds['tas']

# test plot some data
plt.close('all')
projection=ccrs.PlateCarree(central_longitude=0.0)
fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': projection}, layout='constrained')

data = da.isel(time=20)
ax.set_global()
im = egh.healpix_show(data.values,ax=ax)
ax.set_title(f'UM N2560 RAL3 healpix zoom = {zoom}')
ax.coastlines()
ax.gridlines(draw_labels=True)
fig.colorbar(im,orientation='vertical')

plt.show()


