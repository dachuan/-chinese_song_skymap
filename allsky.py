import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())


from skyfield.api import Star,Topos
from skyfield.data import hipparcos
from skyfield.units import Angle

# load hip star data
asterisms= pd.read_csv('./res/song_con.txt',header=None) # song star data
asterisms.columns=['constellation','num_pairs','stars','name','ras','decs','xingxiu','mags']
print(asterisms.shape)
print(asterisms.loc[0,'name'])


# Ursa minor
#hips_umi=[11767, 85822, 85822, 82080, 82080, 77055, 77055, 79822, 79822, 75097, 75097, 72607, 72607, 77055]

# construct stars 
#umi_stars = [Star.from_dataframe(df.loc[v]) for v in np.unique(hips_umi)]

# time scale is important to calculate
ts = load.timescale()
t_song = ts.utc(1000,1,1,20,0) # song dynasty
t_now = ts.now()

planets = load('de421.bsp')
earth = planets['earth']

kaifeng = earth + Topos(longitude_degrees=(114,30,0),
                        latitude_degrees=(+34,8,0)) # north song capital

"""
ras_beiji=[]
decs_beiji=[]
ras_umi = []
decs_umi = []
ras_beidou = []
decs_beidou = []
ras_gouchen = []
decs_gouchen = []

for star in beiji_stars:
    astrometric = kaifeng.at(t_now).observe(star)
    apparent = astrometric.apparent()
    ra,dec,_ = apparent.radec(epoch=t_song)
    ras_beiji.append(ra.radians)
    decs_beiji.append(dec.degrees)


for star in umi_stars:
    astrometric = kaifeng.at(t_now).observe(star)
    apparent = astrometric.apparent()
    ra,dec,_ = apparent.radec(epoch=t_song)
    ras_umi.append(ra.radians)
    decs_umi.append(dec.degrees)

for star in beidou_stars:
    astrometric = kaifeng.at(t_now).observe(star)
    apparent = astrometric.apparent()
    ra,dec,_ = apparent.radec(epoch=t_song)
    ras_beidou.append(ra.radians)
    decs_beidou.append(dec.degrees)

for star in gouchen_stars:
    astrometric = kaifeng.at(t_now).observe(star)
    apparent = astrometric.apparent()
    ra,dec,_ = apparent.radec(epoch=t_song)
    ras_gouchen.append(ra.radians)
    decs_gouchen.append(dec.degrees)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
ax.set_ylim(-45, 45)

plt.show()
"""
