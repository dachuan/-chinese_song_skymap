with open('./res/mkdata.txt','r') as f:
    ls = f.read().splitlines()

ras = []
decs = []
for l in ls:
    _ra, _dec = l.split(',')
    ras.append(float(_ra))
    decs.append(float(_dec))

leaps = []
gap_std = 3
for i in range(1,len(ras)):
    gap = abs(ras[i] - ras[i-1])
    if gap > gap_std:
        leaps.append(i)

print(leaps)
