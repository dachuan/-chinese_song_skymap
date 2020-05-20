import matplotlib.pyplot as plt
import numpy as np

r=45
x= np.arange(60,91,2)
y_linear = 90 - x
y_stereo = r*np.cos(np.radians(x))*2/(np.sin(np.radians(x))+1)
y_gnomonic = r/np.tan(np.radians(x))

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax1.scatter(x,y_linear)
ax1.scatter(x,y_stereo)
ax1.scatter(x,y_gnomonic)

ax2 = fig.add_subplot(122)
ax2.scatter(x,y_stereo)

plt.show()