with open('./res/mkdata.txt','r') as f:
    ls = f.read().splitlines()

ras = []
decs = []
for l in ls:
    _ra, _dec = l.split(',')
    ras.append(float(_ra))
    decs.append(float(_dec))

### divid into circles
leaps = []
gap_std = 1
for i in range(1,len(ras)):
    #gap = abs(decs[i] - decs[i-1])
    gap = abs(ras[i] - ras[i-1])
    if gap > gap_std:
        leaps.append(i)

print(len(leaps))

leaps.insert(0,0)
leaps.append(len(ras))

### slashed ras for each circle
sl_ras =[]
sl_decs =[]
for i in range(1,len(leaps)):
    _ras = ras[leaps[i-1]:leaps[i]]
    sl_ras.append(_ras)
    _decs = decs[leaps[i-1]:leaps[i]]
    sl_decs.append(_decs)

import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_xticks([]) #no ticks
ax.set_yticks([]) #no ticks
ax.set_theta_direction(-1)
ax.set_theta_zero_location('N', offset=-20)
ax.set_ylim(0,140)
ax.set_facecolor('white')

# fill small circles
count = 190 #192
for ras,decs in zip(sl_ras[4:count],sl_decs[4:count]):
    ax.fill(np.radians(ras),[90-i for i in decs],color='blue',alpha=0.1,zorder=11)

'''
# plot two big circles
for ras,decs in zip(sl_ras[:2],sl_decs[:2]):
    #ax.scatter(np.radians(ras),[90-i for i in decs])
    ax.plot(np.radians(ras),[90-i for i in decs])
'''

# re-order sl_ras[0:1]
from tkinter import _flatten
c_ras_1 = list(_flatten(sl_ras[0:2]))
c_decs_1 = list(_flatten(sl_decs[0:2]))
c_ras_2 = list(_flatten(sl_ras[2:4]))
c_decs_2 = list(_flatten(sl_decs[2:4]))

#ax.plot(np.radians(c_ras_1),[90-i for i in c_decs_1],color='blue',alpha=0.1)
#ax.plot(np.radians(c_ras_2),[90-i for i in c_decs_2],color='blue',alpha=0.1)

ax.fill(np.radians(c_ras_1),[90-i for i in c_decs_1],color='white',alpha=1,zorder=10)
ax.fill(np.radians(c_ras_2),[90-i for i in c_decs_2],color='blue',alpha=0.1,zorder=9)


plt.show()
