import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load hip star data
stars= pd.read_csv('./res/song_mag90.csv') # song star data
#print(stars.head())

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
ax.set_xticks([]) #no ticks
ax.set_yticks([]) #no ticks
# linear
ax.set_ylim(0, 100) # -45, 45

# ortho, gnomonic
r = 90
#ax.set_ylim(0,190)
#ax.set_ylim(0,2*r)

ax.set_theta_zero_location('N', offset=30)

#dec_min=0
#dec_max=0

ras=[]
decs=[]
for index,row  in stars.iterrows():

    ra = row['ra_degrees']
    dec = row['dec_degrees']
    mag = row['magnitude']

    # linear
    dec = 45-dec/2
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

    if _alpha < 0.01:
        continue
    else:
        ras.append(ra)
        decs.append(dec)

print(len(ras))

ax.scatter(np.radians(ras),decs,
        color='blue',
        #edgecolor='black',
        s=0.2,
        alpha=0.05,
        #zorder=1
        )
ax.scatter(0,0,color='yellow',s=4)

plt.show()

"""
    # dict to reduce same star
    for ra,dec in dict(zip(ras,decs)).items():

        # linerar
        ##
        #ax.scatter(ra,45-dec,
        #        color='grey',edgecolor='black',
        #        s=1,
        #        alpha=0.8,zorder=1)

        # ortho, gnomonic, stereo
        ##
        ax.scatter(ra,dec,
                color='grey',edgecolor='black',
                s=1,
                alpha=0.8,zorder=1)

    # plot constellation lines
    ##

    # linear
    #_decs = [45-i for i in decs]

    #for n in range(int(len(ras)/2)): #1-2
    #    ax.plot(ras[n*2:(n+1)*2], _decs[n*2:(n+1)*2],
    #            color='green', 
    #            lw=1,
    #            alpha=0.5,zorder=0)

    for n in range(int(len(ras)/2)): #1-2
        ax.plot(ras[n*2:(n+1)*2], decs[n*2:(n+1)*2],
                color='green', 
                lw=1,
                alpha=0.5,zorder=0)

#print('min of dec is :', dec_min)
#print('max of dec is :', dec_max)


plt.show()
"""
