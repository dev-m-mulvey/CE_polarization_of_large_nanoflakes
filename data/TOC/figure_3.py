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
rc('font', family='Nimbus Sans', weight='bold')
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

popt2, pcov2 = curve_fit(func,z,MMA2) 
axs.plot(x_dat,func(x_dat,*popt2),color="green",marker='none',linewidth=3.5,linestyle='-',label=r"$\mathrm{C_{60000}}$")

axs.plot(x_dat,-27.211386245988/(4*x_dat),color="black",linestyle=':',marker="none",linewidth=1.5,label=r"$\mathrm{Graphene}$")

axs.set_xticks([])
axs.set_yticks([])
axs.grid(False)
axs.legend(loc="best", frameon=False, handlelength=1, fontsize=7)
axs.set_ylabel(r"$\mathit{E}_{\mathrm{Pol}}$")

plt.savefig("figure_3.png", dpi=300)
