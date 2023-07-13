import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import pandas as pd
import glob 
import os
import matplotlib.ticker as mtick
from matplotlib import rc
from matplotlib.font_manager import FontProperties


params = {'mathtext.default': 'bf'}
plt.rcParams.update(params)
plt.rcParams.update({'font.size': 8})
rc('font', family='Nimbus Sans', weight='bold')
rc('axes',linewidth=1,edgecolor='k')

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


fig, axs = plt.subplots(1, 1, figsize=(3.33,3.33))
for idx, i in enumerate(xx_yy):
    if i[0] == "PBEZERO":
        axs.plot(i[1],i[2],color="black",markersize=8,linewidth=1,marker="s",markeredgecolor='k',fillstyle='none',markeredgewidth=1,label=r"$\mathrm{PBE0}$")
    elif i[0] == "QMA1":
        axs.plot(i[1],i[2],color="blue",markersize=7,linewidth=1,linestyle='-',marker="o",label=r"$\mathrm{MMA1}$")
    elif i[0] == "QP2":
        axs.plot(i[1],i[2],color="orange",markersize=6,linewidth=1,linestyle='-',marker="^",label=r"$\mathrm{MP2}$")
axs.set_xticks([6,24,54,96,150,216,294,384])
axs.grid(False)
axs.xaxis.set_tick_params(direction="in",length=3,width=1,labelsize=7,pad=6.25)
axs.yaxis.set_tick_params(direction="in",length=3,width=1,labelsize=8,pad=6.25)
print(axs.xaxis.labelpad)
print(axs.yaxis.labelpad)
axs.legend(loc="best", frameon=False)
axs.set_ylabel(r"$\mathrm{\alpha_{xx/yy}} \ \mathrm{\left( a.u.^{3} \right)}$")
axs.set_xlabel(r"$\mathit{N_{C}}$")

fig.set_tight_layout(True)
plt.savefig("figure_1.png", dpi=300)
