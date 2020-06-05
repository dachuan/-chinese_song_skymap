# moon in ecliptic is not divided equally

import matplotlib.pyplot as plt
import numpy as np

from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())


from skyfield.api import Star,Topos
from skyfield.data import hipparcos
from skyfield.units import Angle

ts = load.timescale()

eph = load('de421.bsp')
earth = eph['earth']
moon = eph['moon']

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)

t = ts.utc(2020,3,range(2,2+28))

lons = []
for i in t:
    #print(i)
    lat, lon, d = earth.at(i).observe(moon).ecliptic_latlon()
    #print(lon.degrees)
    ax.scatter(np.radians(lon.degrees),1)
    lons.append(lon.degrees)

gaps = []
for i in range(len(lons)-1):
    gap = lons[i+1] - lons[i]
    if gap < 0:
        gap += 360
    gaps.append(gap)

for g in gaps:
    print(g)

plt.show()
