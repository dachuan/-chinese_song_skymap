import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

asterisms= pd.read_csv('./res/song_con.txt',header=None) # song star data
asterisms.columns=['constellation','num_pairs','stars','name','ras','decs','xingxiu','mags']


fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
ax.set_xticks([]) #no ticks
ax.set_yticks([]) #no ticks
# linear
rim = 110
ax.set_ylim(0, 290) # -45, 45

# ortho, gnomonic
r = 90
#ax.set_ylim(0,120)

ax.set_theta_zero_location('N', offset=30)

for index,row  in asterisms.iterrows():

    # turn string into float-list
    ras = row['ras'].replace('[','').replace(']','').split(',')
    decs = row['decs'].replace('[','').replace(']','').split(',')

    ras = [np.radians(float(i)) for i in ras]
    decs = [float(i) for i in decs]

    # linear
    #decs = [(90-i)*90/rim for i in decs]
    #decs = [90-i for i in decs]

    #shorten
    decs = [i*90/rim for i in decs]

    # ortho
    #decs = [r*np.cos(np.radians(i)) for i in decs]
    # gnomonic
    #decs = [r/np.tan(np.radians(i)) for i in decs]
    # stereo
    decs = [r*np.cos(np.radians(i))*2/(np.sin(np.radians(i))+1) for i in decs]


    # plot stars
    #-----------------------------

    # dict to reduce same star
    for ra,dec in dict(zip(ras,decs)).items():
        ax.scatter(ra,dec,
                color='grey',edgecolor='black',
                s=1,
                alpha=0.8,zorder=1)

    # plot constellation lines
    #-----------------------------

    for n in range(int(len(ras)/2)): #1-2
        ax.plot(ras[n*2:(n+1)*2], decs[n*2:(n+1)*2],
                color='green', 
                lw=1,
                alpha=0.5,zorder=0)
plt.show()
