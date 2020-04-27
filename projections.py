import matplotlib.pyplot as plt
import numpy as np

# display beidou 7 star
ras = [165.93265365, 165.4599615, 165.4599615, 178.45725536, 178.45725536, 183.85603795, 183.85603795, 193.5068041, 193.5068041, 200.98091604, 200.98091604, 206.88560880000003]
decs = [61.75111888, 56.38234478, 56.38234478, 53.69473296, 53.69473296, 57.03259792, 57.03259792, 55.95984301, 55.95984301, 54.92541525, 54.92541525, 49.31330288]

fig,ax = plt.subplots(1,2,subplot_kw={'projection':'polar'})


ax[0].set_ylim(0,90)
ax[0].scatter(np.radians(ras),[90-i for i in decs],s=4)
ax[1].set_ylim(0,190)
ax[1].scatter(np.radians(ras),[90-i for i in decs],s=4)
#
"""
fig,ax = plt.subplots(3,2,subplot_kw={'projection':'polar'})

ax[0][0].set_ylim(-45,45)
ax[0][0].scatter(np.radians(ras),[45-i for i in decs],s=4)

ax[0][1].set_ylim(0,120)
ax[0][1].scatter(np.radians(ras),[90-i for i in decs],s=4)

ax[1][0].set_ylim(-45,25)
ax[1][0].scatter(np.radians(ras),[45-i for i in decs],s=4)

ax[1][1].set_ylim(-45,15)
ax[1][1].scatter(np.radians(ras),[45-i for i in decs],s=4)

ax[2][0].set_ylim(-45,5)
ax[2][0].scatter(np.radians(ras),[45-i for i in decs],s=4)

ax[2][1].set_ylim(-45,-5)
ax[2][1].scatter(np.radians(ras),[45-i for i in decs],s=4)
"""

"""
fig = plt.figure(
        figsize=(10,10)
        )


ax1 = fig.add_subplot(141,projection='polar')
ax1.set_ylim(-45,45)
ax1.scatter(np.radians(ras),[45-i for i in decs],s=4)

ax2 = fig.add_subplot(142,projection='polar')
ax2.set_ylim(-45,35)
ax2.scatter(np.radians(ras),[45-i for i in decs],s=4)

ax3 = fig.add_subplot(143,projection='polar')
ax3.set_ylim(-45,25)
ax3.scatter(np.radians(ras),[45-i for i in decs],s=4)

ax4 = fig.add_subplot(144,projection='polar')
ax4.set_ylim(-45,15)
ax4.scatter(np.radians(ras),[45-i for i in decs],s=4)
"""

"""
ax2 = fig.add_subplot(222,projection='polar')
ax2.set_ylim(-45,45)
ax2.scatter(np.radians(ras),[45 -i for i in decs],s=4)

ax3 = fig.add_subplot(223,polar=True)
#ax3.set_ylim(-45,45)
ax3.scatter(np.radians(ras),decs)

ax4 = fig.add_subplot(224,polar=True)
ax4.set_ylim(-45,45)
ax4.scatter(np.radians(ras),[65 -i for i in decs],s=4)
"""

plt.show()
