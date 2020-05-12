import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# load hip star data
asterisms= pd.read_csv('./res/song_con.txt',header=None) # song star data
asterisms.columns=['constellation','num_pairs','stars','name','ras','decs','xingxiu','mags']

fig = plt.figure()
ax = fig.add_axes([0,0,1,1],polar=True)
ax.set_theta_direction(-1)
#ax.set_xticks([]) #no ticks
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

        ax.scatter(ra,dec,
                color='grey',edgecolor='black',
                s=1,
                alpha=0.8,zorder=1)

    # plot constellation lines
    ##
    for n in range(int(len(ras)/2)): #1-2
        ax.plot(ras[n*2:(n+1)*2], decs[n*2:(n+1)*2],
                color='green', 
                lw=1,
                alpha=0.5,zorder=0)

# plot star marks
#---------------------------------------- 
m_hips = [65474,69427,72622,78265,80112,82514,88635,92041,100345,102618,106278,109074,113963,1067,4463,8903,12719,17499,20889,26207,26727,30343,41822,42313,46390,48356,53740,59803]
m_ras = [3.30895828,14.30178237,28.65978771,40.86296031,56.21884811,67.15388879,83.78449043,85.18968672,95.73996302,127.8990288,129.41419739,141.8968826,147.86951033,164.94478664,183.95194937,201.2983523,213.22392088,222.71990536,239.71300283,245.29717718,252.96766195,271.45218586,281.41397083,305.25269347,311.91888574,322.88966951,331.44593869,346.1900702]
m_ras = [np.radians(i) for i in m_ras]
ax.set_xticks(m_ras) #no ticks

plt.show()
