import matplotlib.pyplot as plt
import numpy as np

# display beidou 7 star
ras = [165.93265365, 165.4599615, 165.4599615, 178.45725536, 178.45725536, 183.85603795, 183.85603795, 193.5068041, 193.5068041, 200.98091604, 200.98091604, 206.88560880000003]
decs = [61.75111888, 56.38234478, 56.38234478, 53.69473296, 53.69473296, 57.03259792, 57.03259792, 55.95984301, 55.95984301, 54.92541525, 54.92541525, 49.31330288]

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
ax.set_ylim(-45, 45)

for i in range(len(ras)):
    ax.scatter(np.radians(ras[i]), 45-decs[i])

plt.show()
