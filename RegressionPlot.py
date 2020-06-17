import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib._color_data as mcd

from numpy.polynomial.polynomial import polyfit
df = pd.read_csv(r"C:\Users\Ana\OneDrive\MWMDataAPOE.csv")
groups = df.groupby('APOE')
#scatter plot
varX = 'Distance'
varY = 'Duration'
y = df[varY]
x = df[varX]
fig, ax = plt.subplots()

n= len(groups)
print(n)

from random import randint
colors = []

color_names = [name for name in mcd.CSS4_COLORS
           if "xkcd:" + name in mcd.XKCD_COLORS]

color_names = ["red","green","purple"] + color_names

colors = [0]*len(color_names)

for i,o in enumerate(color_names):
    colors[i] = mcd.XKCD_COLORS['xkcd:' +  o]

for i, (name, group) in enumerate(groups):
    color = colors[i]
    ax.plot(group[varX], group[varY], '.', label=name,color=color)
    b, m = polyfit(group[varX], group[varY], 1)
    plt.plot(group[varX], b + m * group[varX], '-', color=color)
ax.legend(numpoints=1, loc='upper left')


import numpy as np
import scipy.stats


plt.xlabel(varX, fontsize = 20)
plt.ylabel(varY, fontsize = 20)
plt.show()
print('done')
path = 'C:/Users/Ana/Documents/APOEwork/'
plt.savefig(path +varX + "_" +varY +".png", bbox_extra_artists=(legend,), bbox_inches="tight",dpi = 150)

