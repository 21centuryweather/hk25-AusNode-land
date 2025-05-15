'''
module use /g/data/hh5/public/modules
module load conda/analysis3
source /scratch/nf33/public/hackathon_env/bin/activate
'''

import intake
from easygems import healpix as egh|
import matplotlib.pyplot as plt
import pandas as pd

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# load the catalog
cat = intake.open_catalog("https://digital-earths-global-hackathon.github.io/catalog/catalog.yaml")["online"]
zoom = 6

# list models that include mrso (soil moisture)
for model in list(cat):
    # if 'ifs' not in model:
    #     continue
    # try zoom level 1
    try: 
        ds = cat[model](zoom = zoom).to_dask()
        print(f'{model} OK')
        # search through data_var attributes.standard_name for substring 'soil' and print them
        for var in ds.data_vars:
            for attr in ds[var].attrs.items():
                if isinstance(attr[1], str):
                    # check if 'soil' is in the string
                    allowed_substrings = ['soil', 'precip','sensible','latent']
                    if any(sub in attr[1] for sub in allowed_substrings):
                        print(f'{model} {var} {attr[0]} {attr[1]}')

    except:
        print(f'{model} zoom level {zoom} not available')
        continue

# to_save = ['swvl1','swvl2','swvl3','swvl4','tp','tprate']

# # set encoding for zlib for compression
# encoding = {var: {'zlib': True, 'complevel': 5} for var in to_save}
# # save subset
# ds[to_save].to_netcdf(f'/scratch/nf33/mjl561/hackathon/{model}/{model}_{zoom}.nc', encoding=encoding)

    

