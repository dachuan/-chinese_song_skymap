import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

np.warnings.filterwarnings('ignore')

# load hip star data
stars= pd.read_csv('./res/song_mag90.csv') # song star data
#print(stars.head())

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
ax.set_xticks([]) #no ticks
ax.set_yticks([]) #no ticks

# linear
#ax.set_ylim(0, 100) # -45, 45

# ortho, gnomonic
r = 90
#ax.set_ylim(0,190)
#ax.set_ylim(0,2*r)

ax.set_theta_zero_location('N', offset=30)

#dec_min=0
#dec_max=0

ras=[]
decs=[]
alphas=[]
for index,row  in stars.iterrows():

    ra = row['ra_degrees']
    dec = row['dec_degrees']
    mag = row['magnitude']

    # linear
    #dec = 45-dec/2
    # ortho
    #decs = [r*np.cos(np.radians(i)) for i in decs]
    # gnomonic
    #decs = [ (i+130)*90/160 for i in decs] # [-60,90] relocate to [70,90]
    #decs = [r/np.tan(np.radians(i)) for i in decs]
    # stereo
    #decs = [ (i+60)*90/150 for i in decs] # [-60,90] relocate to [0,90]
    #decs = [r*np.cos(np.radians(i))*2/(np.sin(np.radians(i))+1) for i in decs]


    # plot stars
    #-----------------------------

    max_mag = 9.0
    min_mag = -1.44
    _alpha = (mag - min_mag)/(max_mag - min_mag)
    _alpha = 1 -_alpha
    _alpha = int(_alpha*10) / 10.0
    ras.append(ra)
    decs.append(dec)
    alphas.append(_alpha)

#print(len(alphas))
#print(alphas[:100])
#print(np.unique(alphas))
#

zzz = sorted(zip(alphas,ras,decs))

s_a , s_r ,s_d = zip(*zzz)

u,i = np.unique(s_a,return_index=True)

print(i)

###
# transform the data to projection
###

prj_type = 'stereo'

if prj_type =='linear':
    # linear
    s_d = [90-i for i in s_d]
    #s_d = [45-i/2 for i in s_d]
    ax.set_ylim(0, max(s_d)+2) # -45, 45
elif prj_type=='ortho':
    # ortho
    r = 90 
    s_d = [r*np.cos(np.radians(i)) for i in s_d]
    ax.set_ylim(0, 180) # -45, 45
elif prj_type=='gnomonic':
    r = 90
    s_d = [r/np.tan(np.radians(i)) for i in s_d]
    #print(max(s_d))
    ax.set_ylim(0, 500) # -45, 45
elif prj_type=='stereo':
    r = 90
    s_d = [r*np.cos(np.radians(i))*2/(np.sin(np.radians(i))+1) for i in s_d]
    print(max(s_d))
    ax.set_ylim(0, 360) # -45, 45
else:
    print('the projection type is not correct!')


for ii in range(1,len(i)):
    _ras = s_r[i[ii-1]:i[ii]]
    _decs = s_d[i[ii-1]:i[ii]]
    #print(i[ii-1])
    #print('alpha :',s_a[i[ii-1]])
    ax.scatter(np.radians(_ras),_decs,
            color='blue',
            #edgecolor='black',
            s=0.2,
            alpha=s_a[i[ii-1]]*0.5+0.01,
            #alpha=0.05,
            #zorder=1
            )

ax.scatter(0,0,color='yellow',s=4)


'''
ax.scatter(np.radians(ras),decs,
        color='blue',
        #edgecolor='black',
        s=0.2,
        alpha=alphas,
        #alpha=0.05,
        #zorder=1
        )
ax.scatter(0,0,color='yellow',s=4)
'''

plt.show()
