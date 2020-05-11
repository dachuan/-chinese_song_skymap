import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#from skyfield_data import get_skyfield_data_path
#from skyfield.api import Loader
#load = Loader(get_skyfield_data_path())


#from skyfield.api import Star,Topos
#from skyfield.data import hipparcos
#from skyfield.units import Angle

# load hip star data
asterisms= pd.read_csv('./res/song_con.txt',header=None) # song star data
asterisms.columns=['constellation','num_pairs','stars','name','ras','decs','xingxiu','mags']

# time scale is important to calculate
#ts = load.timescale()
#t_song = ts.utc(1000,1,1,20,0) # song dynasty
#t_now = ts.now()
#
#planets = load('de421.bsp')
#earth = planets['earth']
#
#kaifeng = earth + Topos(longitude_degrees=(114,30,0),
#                        latitude_degrees=(+34,8,0)) # north song capital

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
ax.set_xticks([]) #no ticks
#ax.set_yticks([]) #no ticks
# linear
ax.set_ylim(0, 80) # -45, 45

# ortho, gnomonic
r = 90
#ax.set_ylim(0,190)
#ax.set_ylim(0,2*r)

ax.set_theta_zero_location('N', offset=30)

#dec_min=0
#dec_max=0

for index,row  in asterisms.iterrows():

    # turn string into float-list
    ras = row['ras'].replace('[','').replace(']','').split(',')
    decs = row['decs'].replace('[','').replace(']','').split(',')

    ras = [np.radians(float(i)) for i in ras]
    decs = [float(i) for i in decs]

    # check the max and min of dec
#    if dec_min > min(decs):
#        dec_min=min(decs)
#
#    if dec_max < max(decs):
#        dec_max = max(decs)

    # linear
    #decs = [90-i for i in decs]
    decs = [45-i/2 for i in decs]
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
