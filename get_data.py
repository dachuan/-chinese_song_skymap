from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())

from skyfield.api import Star
from skyfield.data import hipparcos

with load.open('/anaconda3/envs/astro/lib/python3.8/site-packages/skyfield/data/hip_main.dat.gz') as f:
    df = hipparcos.load_dataframe(f)

print("hip data :",df.shape)

mag65 = df[df['magnitude']<= 6.5]
print("mag under 6.5 :",mag65.shape)

mag65.to_csv('./res/hip_mag65.csv')
