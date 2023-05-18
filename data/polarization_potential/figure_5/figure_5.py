import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob 
import os
from matplotlib import rc
from matplotlib.font_manager import FontProperties


params = {'mathtext.default': 'bf'}
plt.rcParams.update(params)
plt.rcParams.update({'font.size': 50})
rc('font', weight='bold')

x_dat=np.arange(5,10,0.01)

pot = []
for filename in sorted(glob.glob("figure_5.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    num_rows, num_cols = data_array.shape
    z = data_array[:,0]
    MMA2 = data_array[:,1]*27.211386245988
    impot = data_array[:,2]*27.211386245988


fig, axs = plt.subplots(1, 1, figsize=(25,25))
axs.scatter(z,impot,color="black",s=2000,linestyle='-',marker="s",label=r"$\mathrm{-6.8028/|z-1.98|}$") 
axs.plot(x_dat,-27.211386245988/(4*np.abs(x_dat-1.9804329786078072)),color="black",markersize=2,linewidth=8,linestyle='-')

axs.scatter(z,MMA2,color="green",s=2000,marker="^", label=r'$\mathrm{MMA2}$')
axs.set_xlabel(r"$z \ a_0$")    
axs.set_xticks([5,6,7,8,9,10])
axs.grid(which='major', linestyle='-')
axs.legend(loc="best", frameon=False, fontsize='large')
axs.set_ylabel(r"$\mathrm{V} \ \mathrm{\left( eV \right)}$")

fig.set_tight_layout(True)
plt.savefig("figure_5.png", dpi=300)