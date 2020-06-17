import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import matplotlib._color_data as mcd
import scipy.stats as stats

def plot_ci_manual(t, s_err, n, x, x2, y2, ax=None, color="#b9cfe7"):
    if ax is None:
        ax = plt.gca()

    ci = t * s_err * np.sqrt(1/n + (x2 - np.mean(x))**2 / np.sum((x - np.mean(x))**2))
    ax.fill_between(x2, y2 + ci, y2 - ci, color=color, edgecolor="", alpha = 0.2)

    return ax


#from numpy.polynomial.polynomial import polyfit
df = pd.read_csv(r"C:\Users\Ana\OneDrive\MWMDataAPOE.csv")
groups = df.groupby('APOE')
#scatter plot
varX = 'Distance'
varY = 'Duration'

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
    y = group[varY]
    x = group[varX]
    color = colors[i]
    ax.plot(x, y, '.', label=name,color=color)
    p,cov = np.polyfit(x, y, 1,cov = True)

    y_model = np.polyval(p, x) 

    # Statistics
    n = y.size                                           # number of observations
    m = p.size                                                 # number of parameters
    dof = n - m                                                # degrees of freedom
    t = stats.t.ppf(0.975, n - m)                              # used for CI and PI bands

    # Estimates of Error in Data/Model
    resid = y - y_model                           
    chi2 = np.sum((resid / y_model)**2)                        # chi-squared; estimates error in data
    chi2_red = chi2 / dof                                      # reduced chi-squared; measures goodness of fit
    s_err = np.sqrt(np.sum(resid**2) / dof)                    # standard deviation of the error


    # Fit
    ax.plot(x, y_model, "-", color=color, linewidth=1.5, alpha=0.5, label="Fit")  

    x2 = np.linspace(np.min(x), np.max(x), 100)
    y2 = np.polyval(p, x2) 

    plot_ci_manual(t, s_err, n, x, x2, y2, ax=ax, color=color)

ax.legend(numpoints=1, loc='upper left')




plt.xlabel(varX, fontsize = 20)
plt.ylabel(varY, fontsize = 20)
plt.show()

plt.tight_layout()
path = 'C:/Users/Ana/Documents/APOEwork/'
plt.savefig(path +varX + "_" +varY +"CI.png", bbox_extra_artists=(legend,), bbox_inches="tight",dpi = 150)

