import matplotlib.pyplot as plt
import numpy as np

# display beidou 7 star
ras = [165.93265365, 165.4599615, 165.4599615, 178.45725536, 178.45725536, 183.85603795, 183.85603795, 193.5068041, 193.5068041, 200.98091604, 200.98091604, 206.88560880000003]
decs = [61.75111888, 56.38234478, 56.38234478, 53.69473296, 53.69473296, 57.03259792, 57.03259792, 55.95984301, 55.95984301, 54.92541525, 54.92541525, 49.31330288]


fig = plt.figure(
        figsize=(10,10)
        )

# dec as r, linear
ax1 = fig.add_subplot(221,projection='polar')
ax1.set_ylim(0,90)
ax1.scatter(np.radians(ras),[90-i for i in decs],s=4)
ax1.set_title('Linear')

# ortho
ax2 = fig.add_subplot(222,projection='polar')
ax2.set_ylim(0,90)
r = 90
ax2.scatter(np.radians(ras),[r*np.cos(np.radians(i)) for i in decs],s=4)
ax2.set_title('Ortho')

# gnomonic
ax3 = fig.add_subplot(223,projection='polar')
ax3.set_ylim(0,90)
r = 90
ax3.scatter(np.radians(ras),[r/np.tan(np.radians(i)) for i in decs],s=4)
ax3.set_title('Gnomonic')

# stero
ax4 = fig.add_subplot(224,projection='polar')
ax4.set_ylim(0,90)
r = 90
ax4.scatter(np.radians(ras),[r*np.cos(np.radians(i))*2/(np.sin(np.radians(i))+1) for i in decs],s=4)
ax4.set_title('Stereo')

plt.show()
