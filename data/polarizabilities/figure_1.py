import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob 
import os
from matplotlib import rc
from matplotlib.font_manager import FontProperties


params = {'mathtext.default': 'bf'}
plt.rcParams.update(params)
plt.rcParams.update({'font.size': 70})
rc('font', weight='bold')
rc('axes',linewidth=5,edgecolor='k')

xx_yy = []
for filename in sorted(glob.glob("*.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    num_rows, num_cols = data_array.shape
    if num_cols == 2 and num_rows > 5:
        n = data_array[:,0]
        print(n)
        axx = data_array[:,1]
        print(axx)
        xx_yy.append([Source,n,axx])
    if num_cols == 2 and num_rows == 5:
        n = data_array[:,0]
        axx = data_array[:,1]
        xx_yy.append([Source,n,axx])


fig, axs = plt.subplots(1, 1, figsize=(25,25))
for idx, i in enumerate(xx_yy):
    if i[0] == "PBEZERO":
        axs.plot(i[1],i[2],color="black",markersize=65,linewidth=5,marker="s",label=r"$\mathrm{PBE0}$")
    elif i[0] == "QMA1":
        axs.plot(i[1],i[2],color="silver",markersize=55,linewidth=5,linestyle='-',marker="o",label=r"$\mathrm{MMA1}$")
    elif i[0] == "QP2":
        axs.plot(i[1],i[2],color="orange",markersize=45,linewidth=5,linestyle='-',marker="^",label=r"$\mathrm{MP2}$")
    axs.set_xlabel(r"$N_{C}$")    
    axs.xaxis.set_tick_params(labelrotation=35,direction="in",length=25,width=8,labelsize=60)
    axs.yaxis.set_tick_params(direction="in",length=25,width=8)
    axs.set_xticks([6,24,54,96,150,216,294,384])
    axs.grid(False)
    axs.legend(loc="best", frameon=False, fontsize='large')
    axs.set_ylabel(r"$\mathrm{\alpha_{xx/yy}} \ \mathrm{\left( a.u.^{3} \right)}$")

fig.set_tight_layout(True)
plt.savefig("figure_1.png", dpi=300)
