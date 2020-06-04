from skyfield_data import get_skyfield_data_path
from skyfield.api import Loader
load = Loader(get_skyfield_data_path())
from skyfield.api import Star, Topos

import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np
import pandas as pd

import datetime as dt

#----------------------------------------------------------------------------------------#
#-----------ecliptic is the sun orbit----------------------------------------------------#
#----------------------------------------------------------------------------------------#
# load sun, moon data
time_scale = load.timescale()
planets = load('de421.bsp')

earth = planets['earth']
sun = planets['sun']
moon = planets['moon']

kaifeng = earth + Topos(longitude_degrees=(114,30,0),
                        latitude_degrees=(+34,8,0))

## one year 
d1 = dt.datetime(2020,1,1,0,0,0)
d_oneyear = [d1 +dt.timedelta(days=1)*i for i in range(366)]
t_oneyear = [time_scale.utc(i.year, i.month, i.day, i.hour, i.minute, i.second)
        for i in d_oneyear]

## get sun ra dec in everyday of one year
ras_sun = []
decs_sun = []
for t in t_oneyear:
    radec = kaifeng.at(t).observe(sun).apparent().radec()
    ra = np.radians(radec[0]._degrees)
    dec = radec[1].degrees
    ras_sun.append(ra)
    decs_sun.append(dec)

# linear trans
decs_sun = [45 -i/2 for i in decs_sun]

## get moon ra dec in 30 days

d_onemonth = [d1 +dt.timedelta(days=1)*i for i in range(366)]
#d_onemonth = [d1 +dt.timedelta(days=1)*i for i in range(31)]
t_onemonth = [time_scale.utc(i.year, i.month, i.day, i.hour, i.minute, i.second)
        for i in d_onemonth]
ras_moon = []
decs_moon = []

for t in t_onemonth:
    radec = kaifeng.at(t).observe(moon).apparent().radec()
    ra = np.radians(radec[0]._degrees)
    dec = radec[1].degrees
    ras_moon.append(ra)
    decs_moon.append(dec)

# linear trans
decs_moon = [45 -i/2 for i in decs_moon]

#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
#----------------------------------------------------------------------------------------#
# load hip star data
asterisms= pd.read_csv('./res/song_con.txt',header=None) # song star data
asterisms.columns=['constellation','num_pairs','stars','name','ras','decs','xingxiu','mags']

fig = plt.figure()
ax = fig.add_axes([0.1,0.1,0.8,0.8],polar=True)
ax.set_theta_direction(-1)
#ax.set_xticks([]) #no ticks
#ax.set_yticks([]) #no ticks


# linear
ax.set_ylim(0, 70) # -45, 45

# ortho, gnomonic
r = 90
#ax.set_ylim(0,190)
#ax.set_ylim(0,2*r)

ax.set_theta_zero_location('N', offset=30)

#dec_min=0
#dec_max=0

# sun orbit
ax.plot(ras_sun,decs_sun,color='yellow',linewidth=2)
# moon orbit
ax.plot(ras_moon,decs_moon,color='brown',linewidth=2)

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
    if row['xingxiu'] == True:
        line_color='#FF0088'
    else:
        line_color='green'
    for n in range(int(len(ras)/2)): #1-2
        ax.plot(ras[n*2:(n+1)*2], decs[n*2:(n+1)*2],
                color=line_color, 
                lw=1,
                alpha=0.5,zorder=0)

# plot star marks
#---------------------------------------- 
m_hips = [65474,69427,72622,78265,80112,82514,88635,92041,100345,102618,106278,109074,113963,1067,4463,8903,12719,17499,20889,26207,26727,30343,41822,42313,46390,48356,53740,59803]
m_ras = [188.3068061067326,200.10286152716668,209.13717440032724,224.93105499168777,230.40511201883487,236.4102840543427,255.45898085569576,265.77707463598375,291.0499458552401,298.23870887312785,309.5898513001086,318.5132138257615,333.8270860702388,350.58458545769895,1.227193202935566,15.185331686734072,26.60367114290539,41.70683460999782,52.81805740006933,70.10789528501147,72.63958396475854,80.65530070891286,113.41656513131221,116.03769760749587,129.56936528353552,135.86100829172346,152.72622129154024,171.23281028317868]
m_names=['角','亢','氐','房','心','尾','箕','斗','牛','女','虚','危','室','壁','奎','娄','胃','昴','毕','觜','参','井','鬼','柳','星','张','翼','轸']
#m_names=[i for i in range(28)]
m_ras = [np.radians(i) for i in m_ras]
#ax.set_xticks(m_ras,m_names) #no ticks

cnfont = fm.FontProperties(fname='/System/Library/Fonts/PingFang.ttc')
plt.xticks(m_ras,m_names,FontProperties=cnfont)

plt.show()
