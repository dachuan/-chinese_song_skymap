import pandas as pd

with open('./res/con_hip.txt') as f:
    ss = f.readlines()

hips=[]

for s in ss:
    hips.append(s.split()) # not split(' ') , which divide one space

for hip in hips:
    hip[-1] = hip[-1].replace('\n','')


#df = pd.read_csv('hip_all.csv')
df = pd.read_csv('./res/song_mag90.csv')

ras = []
decs = []

for hip in hips:
    ra = []
    dec = []
    for star in hip:
        _ra = df[df['hip'] == float(star)]['ra_degrees'].iloc[0]
        _dec = df[df['hip'] == float(star)]['dec_degrees'].iloc[0]
        ra.append(_ra)
        dec.append(_dec)
    ras.append(ra)
    decs.append(dec)

with open ('./res/song_ras.txt','w') as f:
    for ra in ras:
        f.writelines(str(ra) + '\n')


with open ('./res/song_decs.txt','w') as f:
    for dec in decs:
        f.writelines(str(dec) + '\n')
