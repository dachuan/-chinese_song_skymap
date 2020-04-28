import matplotlib.pyplot as plt
import numpy as np

# display beidou 7 star
ras = [165.93265365, 165.4599615, 165.4599615, 178.45725536, 178.45725536, 183.85603795, 183.85603795, 193.5068041, 193.5068041, 200.98091604, 200.98091604, 206.88560880000003]
decs = [61.75111888, 56.38234478, 56.38234478, 53.69473296, 53.69473296, 57.03259792, 57.03259792, 55.95984301, 55.95984301, 54.92541525, 54.92541525, 49.31330288]

fig = plt.figure()

# check following two is the same

#    /
#   /--
ax1 = fig.add_subplot(121,projection='polar')
#ax1.set_theta_direction(-1)
ax1.set_ylim(0, 60)
ax1.scatter(np.radians(ras), [90-i for i in decs], s=1)

# |
# |-----
_cos = np.cos(np.radians(ras))
_sin = np.sin(np.radians(ras))
_r = np.array([90-i for i in decs])
x = _r*_cos
y = _r*_sin
ax2 = fig.add_subplot(122)
ax2.scatter(x,y,s=1)

plt.show()
