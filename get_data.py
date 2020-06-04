from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())

from skyfield.api import Star,Topos
from skyfield.data import hipparcos

# loading data
with load.open('/anaconda3/envs/astro/lib/python3.8/site-packages/skyfield/data/hip_main.dat.gz') as f:
    df = hipparcos.load_dataframe(f)

#print("hip data :",df.shape)

#********************#
# now time data      # 
#********************#

df.to_csv('./res/hip_all.csv')

mag90 = df[df['magnitude']<= 9.0]
#print("mag under 9.0 :",mag90.shape)

mag90.to_csv('./res/hip_mag90.csv')


#********************#
## data in history   #
#********************#

song_m9 = mag90.copy()

# time scale is important to calculate
ts = load.timescale()
t_song = ts.utc(1000,1,1,0,0) # song dynasty
t_now = ts.now()

planets = load('de421.bsp')
earth = planets['earth']

kaifeng = earth + Topos(longitude_degrees=(114,30,0),
                        latitude_degrees=(+34,8,0)) # north song capital


for index,row in mag90.iterrows():
    _star = Star.from_dataframe(mag90.loc[index])
    astrometric = kaifeng.at(t_now).observe(_star)
    apparent = astrometric.apparent()
    ra,dec,_ = apparent.radec(epoch=t_song)
    song_m9.loc[index,'ra_degrees'] = ra._degrees
    song_m9.loc[index,'dec_degrees'] = dec.degrees

song_m9.to_csv('./res/song_mag90.csv')
#import random
#i = random.randint(1,6000)
#print(mag90.iloc[i])
#print('----------')
#print(song_m9.iloc[i])

