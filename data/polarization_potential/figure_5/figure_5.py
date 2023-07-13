import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import glob 
import os
import matplotlib.ticker as mtick
from matplotlib import rc
from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit


params = {'mathtext.default': 'bf'}
plt.rcParams.update(params)
plt.rcParams.update({'font.size': 10})
rc('font', family='Nimbus Sans', weight='bold')
rc('axes',linewidth=1,edgecolor='k')

x_dat=np.arange(5,10,0.01)

def func_fixed(x,b):  
    return -6.802846561497/np.abs(x-b)

pot = []
for filename in sorted(glob.glob("figure_5.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    num_rows, num_cols = data_array.shape
    z = data_array[:,0]
    MMA2 = data_array[:,1]*27.211386245988
    impot = data_array[:,2]*27.211386245988

fig, axs = plt.subplots(1, 1, figsize=(3.33,3.33))

axs.plot(x_dat,-27.211386245988/(4*np.abs(x_dat-1.9804329786078072)),color="black",linestyle='-',markersize=0.01,marker="s",linewidth=2,mfc='none',markeredgewidth=1.5,label=r"$\mathrm{-6.8028/|}\mathit{z}\mathrm{-1.98|}$")
axs.scatter(z,impot,color="black",s=60,facecolors='none',edgecolor='k',linewidth=1.5,marker="s") 

popt4, pcov4 = curve_fit(func_fixed,z,MMA2) 
axs.plot(x_dat,func_fixed(x_dat,*popt4),color="green",marker='^',markersize=0.01,linewidth=2,linestyle='-',label=r"$MMA2: -6.8028\mathrm{{/|}}\mathit{{z}}-{:.4f}\mathrm{{|}}$".format(popt4[0]))
axs.scatter(z,MMA2,color="green",s=50,marker="^")

axs.set_xlabel(r"$\mathit{z} \ (a_0)$")  
axs.set_xticks([5,6,7,8,9,10])
axs.xaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.yaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.grid(False)
axs.legend(loc="best", frameon=False, fontsize=7, markerscale=600)
axs.set_ylabel(r"$\mathit{E}_{pol} \ \mathrm{\left( eV \right)}$")

fig.set_tight_layout(True)
plt.savefig("figure_5.png", dpi=300)
