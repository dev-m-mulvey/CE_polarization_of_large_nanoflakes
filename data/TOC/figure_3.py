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
plt.rcParams.update({'font.size': 8})
rc('font', weight='bold')
rc('axes',linewidth=1,edgecolor='k')

x_dat=np.arange(5,10,0.01)

def func(x, a):  
    return a/x

pot = []
for filename in sorted(glob.glob("figure_3.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    num_rows, num_cols = data_array.shape
    z = data_array[:,0]
    MMA1 = data_array[:,1]*27.211386245988
    MMA2 = data_array[:,2]*27.211386245988
    impot = data_array[:,3]*27.211386245988


fig, axs = plt.subplots(figsize=(1.625,0.875))

axs.plot(x_dat,-27.211386245988/(4*x_dat),color="black",linestyle='-',markersize=0.01,marker="s",linewidth=1,mfc='none',markeredgewidth=1,label=r"$Classical$")
axs.scatter(z,impot,color="black",s=30,facecolors='none',edgecolor='k',linewidth=1,marker="s") 

popt2, pcov2 = curve_fit(func,z,MMA2) 
axs.plot(x_dat,func(x_dat,*popt2),color="green",marker='^',markersize=0.01,linewidth=1,linestyle='-',label=r"$MM\AA 2$")
axs.scatter(z,MMA2,color="green",s=15,marker="^")

axs.set_xlabel(r"$\mathit{z} \ (a_0)$")    
axs.set_xticks([5,6,7,8,9,10])
axs.set_yticks([-0.6,-1.0,-1.4])
axs.xaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.yaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.grid(False)
axs.legend(loc=4, frameon=False, markerscale=400, fontsize=6)
axs.set_ylabel(r"$\mathit{E}_{pol} \ \mathrm{\left( eV \right)}$")

plt.savefig("figure_3.png", dpi=300,bbox_inches='tight')
