import matplotlib.pyplot as plt
import numpy as np

from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())


from skyfield.api import Star,Topos
from skyfield.data import hipparcos
from skyfield.units import Angle

# load hip star data
with load.open('/anaconda3/envs/astro/lib/python3.8/site-packages/skyfield/data/hip_main.dat.gz') as f:
    df = hipparcos.load_dataframe(f)

# beidou 7 star
#hips=[54061, 53910, 53910, 58001, 58001, 59774, 59774, 62956, 62956, 65378, 65378, 67301]
#ras = [165.93265365, 165.4599615, 165.4599615, 178.45725536, 178.45725536, 183.85603795, 183.85603795, 193.5068041, 193.5068041, 200.98091604, 200.98091604, 206.88560880000003]
#decs = [61.75111888, 56.38234478, 56.38234478, 53.69473296, 53.69473296, 57.03259792, 57.03259792, 55.95984301, 55.95984301, 54.92541525, 54.92541525, 49.31330288]

# beiji
hips_beiji= [75097, 72607, 72607, 70692, 70692, 69112, 69112, 62572]
ras= [230.1822884, 222.67664751, 222.67664751, 216.88134383, 216.88134383, 212.21253759, 212.21253759, 192.30750199]
decs= [71.83397308, 74.15547596, 74.15547596, 75.69593921, 75.69593921, 77.54743312, 77.54743312, 83.41285818]

# Ursa minor
hips_umi=[11767, 85822, 85822, 82080, 82080, 77055, 77055, 79822, 79822, 75097, 75097, 72607, 72607, 77055]

# construct stars 
umi_stars = [Star.from_dataframe(df.loc[v]) for v in np.unique(hips_umi)]
beiji_stars = [Star.from_dataframe(df.loc[v]) for v in np.unique(hips_beiji)]

# time scale is important to calculate
ts = load.timescale()
t_song = ts.utc(1000,1,1,0,0) # song dynasty
t_now = ts.now()

planets = load('de421.bsp')
earth = planets['earth']

kaifeng = earth + Topos(longitude_degrees=(114,30,0),
                        latitude_degrees=(+34,8,0)) # north song capital

ras_now=[]
decs_now=[]
ras_song = []
decs_song = []
for star in beiji_stars:
    astrometric = kaifeng.at(t_now).observe(star)
    apparent = astrometric.apparent()
    #ra,dec,_ = apparent.radec()
    #ras_now.append(ra.radians)
    #decs_now.append(dec.degrees)
    #print(ra._degrees)
    #print('----------')
    ra,dec,_ = apparent.radec(epoch=t_song)
    ras_song.append(ra.radians)
    decs_song.append(dec.degrees)
    #print(ra._degrees)
    #print('**********')


for star in umi_stars:
    astrometric = kaifeng.at(t_now).observe(star)
    apparent = astrometric.apparent()
    ra,dec,_ = apparent.radec()
    ras_now.append(ra.radians)
    decs_now.append(dec.degrees)

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
ax.set_ylim(-45, 0)
#ax.set_ylim(-45, 45)


for i in range(len(ras_song)):
    ax.scatter(ras_song[i], 45-decs_song[i], color='red')

for i in range(len(ras_now)):
    ax.scatter(ras_now[i], 45-decs_now[i], color='blue')

#ax.scatter(ras_song[0], 45-decs_song[0], color='red')

plt.show()
