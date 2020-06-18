import matplotlib.pyplot as plt
import numpy as np

from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())


from skyfield.api import Star,Topos
from skyfield.data import hipparcos
from skyfield.units import Angle

# load hip star data
#with load.open('/anaconda3/envs/astro/lib/python3.8/site-packages/skyfield/data/hip_main.dat.gz') as f:
with load.open(hipparcos.URL) as f:
    #the download hi_main.dat.gz in ..../site-packages/skyfield/data
    df = hipparcos.load_dataframe(f)

# beidou 7 star
hips_beidou=[54061, 53910, 53910, 58001, 58001, 59774, 59774, 62956, 62956, 65378, 65378, 67301]

# beiji
hips_beiji= [75097, 72607, 72607, 70692, 70692, 69112, 69112, 62572]

# gouchen
hips_gouchen=[112833, 5372, 5372, 11767, 11767, 85822, 85822, 82080, 82080, 77055]

# Ursa minor
hips_umi=[11767, 85822, 85822, 82080, 82080, 77055, 77055, 79822, 79822, 75097, 75097, 72607, 72607, 77055]

# construct stars 
umi_stars = [Star.from_dataframe(df.loc[v]) for v in np.unique(hips_umi)]
beiji_stars = [Star.from_dataframe(df.loc[v]) for v in np.unique(hips_beiji)]
beidou_stars = [Star.from_dataframe(df.loc[v]) for v in np.unique(hips_beidou)]
gouchen_stars  = [Star.from_dataframe(df.loc[v]) for v in np.unique(hips_gouchen)]

# time scale is important to calculate
ts = load.timescale()
t_song = ts.utc(1000,1,1,20,0) # song dynasty
t_now = ts.now()

planets = load('de421.bsp')
earth = planets['earth']

kaifeng = earth + Topos(longitude_degrees=(114,30,0),
                        latitude_degrees=(+34,8,0)) # north song capital

ras_beiji=[]
decs_beiji=[]

alt_beiji=[]
az_beiji=[]

ras_umi = []
decs_umi = []
ras_beidou = []
decs_beidou = []
ras_gouchen = []
decs_gouchen = []

for star in umi_stars:
    astrometric = kaifeng.at(ts.utc(2020,4,16,16,30,37.5)).observe(star)
    #astrometric = kaifeng.at(t_now).observe(star)
    apparent = astrometric.apparent()
    alt,az,_ = apparent.altaz()
    alt_beiji.append(alt.degrees)
    az_beiji.append(az.radians)
    #ra,dec,_ = apparent.radec()
    #ra,dec,_ = apparent.radec(epoch=t_song)
    #ras_beiji.append(ra.radians)
    #decs_beiji.append(dec.degrees)

print(alt_beiji)
print(az_beiji)
"""
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
"""

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
#ax.set_ylim(0, 40)
ax.set_ylim(-45, 45)


for i in range(len(alt_beiji)):
    ax.scatter(az_beiji[i], 45-alt_beiji[i], color='red')
    #ax.scatter(ras_beiji[i], 45-decs_beiji[i], color='red')

#for i in range(len(ras_umi)):
    #ax.scatter(ras_umi[i], 45-decs_umi[i], color='blue')

#for i in range(len(ras_beidou)):
#    ax.scatter(ras_beidou[i], 45-decs_beidou[i], color='blue')
#
#for i in range(len(ras_gouchen)):
#    ax.scatter(ras_gouchen[i], 45-decs_gouchen[i], color='green')

plt.show()
