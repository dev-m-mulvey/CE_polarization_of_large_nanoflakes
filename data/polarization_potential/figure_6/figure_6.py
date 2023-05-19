import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob 
import os
from matplotlib import rc
from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit

params = {'mathtext.default': 'bf'}
plt.rcParams.update(params)
plt.rcParams.update({'font.size': 70})
rc('font', weight='bold')
rc('axes',linewidth=5,edgecolor='k')

x_impot=np.arange(4.99,10.01,0.01)
y_impot=(-1/(2*x_impot))*27.211386245988

def func(x, a):  
    return a/x

pot = []
for filename in sorted(glob.glob("figure_6.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    num_rows, num_cols = data_array.shape
    z = data_array[:,0]
    MMA2 = data_array[:,1]*27.211386245988
    impot = data_array[:,2]*27.211386245988


fig, axs = plt.subplots(1, 1, figsize=(25,25))
axs.plot(x_impot,y_impot,color="black",linewidth=15,linestyle='-',label=r"$\mathrm{-13.6057/z}$")

popt, pcov = curve_fit(func,z,MMA2) 
axs.plot(x_impot,func(x_impot,*popt),color="red",markersize=2,linewidth=8,linestyle='--',label=r"$\mathrm{{MMA2:{:.4f}/z}}$".format(popt[0]))
axs.scatter(z,MMA2,color="red",s=2000,marker="^")
axs.set_xlabel(r"$z \ (a_0)$")    
axs.set_xticks([5,6,7,8,9,10])
axs.xaxis.set_tick_params(direction="in",length=25,width=8)
axs.yaxis.set_tick_params(direction="in",length=25,width=8)
axs.grid(False)
axs.legend(loc="best", frameon=False, fontsize=65)
axs.set_ylabel(r"$\mathrm{V} \ \mathrm{\left( eV \right)}$")

fig.set_tight_layout(True)
plt.savefig("figure_6.png", dpi=300)
