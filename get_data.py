from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())

from skyfield.api import Star
from skyfield.data import hipparcos

with load.open('/anaconda3/envs/astro/lib/python3.8/site-packages/skyfield/data/hip_main.dat.gz') as f:
    df = hipparcos.load_dataframe(f)

print("hip data :",df.shape)
df.to_csv('./res/hip_all.csv')

mag90 = df[df['magnitude']<= 9.0]
print("mag under 9.0 :",mag90.shape)

mag90.to_csv('./res/hip_mag90.csv')
