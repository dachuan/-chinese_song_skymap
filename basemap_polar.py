# source activate plt to use basemap
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
import numpy as np

ras = [165.93265365, 165.4599615, 165.4599615, 178.45725536, 178.45725536, 183.85603795, 183.85603795, 193.5068041, 193.5068041, 200.98091604, 200.98091604, 206.88560880000003]
decs = [61.75111888, 56.38234478, 56.38234478, 53.69473296, 53.69473296, 57.03259792, 57.03259792, 55.95984301, 55.95984301, 54.92541525, 54.92541525, 49.31330288]

width = 4000000
m = Basemap(width=width, height=width, 
                projection='npstere', #spstere
                boundinglat=0,
                #projection='aeqd',
                #lat_0=90, lon_0=ras[3])
                lat_0=decs[3], lon_0=ras[0])
m.drawparallels(np.arange(-80,81,10))
m.drawmeridians(np.arange(-180,180,10))
x, y = m(ras, decs)
m.plot(x, y, marker='o', linestyle='--', color='b')

plt.show()
