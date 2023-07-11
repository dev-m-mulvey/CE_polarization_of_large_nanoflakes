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
plt.rcParams.update({'font.size': 10})
rc('font', weight='bold')
rc('axes',linewidth=1,edgecolor='k')

pot = []
for filename in sorted(glob.glob("figure_2_a.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    num_rows, num_cols = data_array.shape
    z = data_array[:,0]
    c150 = data_array[:,1]*27.211386245988
    c600 = data_array[:,2]*27.211386245988
    c2400 = data_array[:,3]*27.211386245988
    c15000 = data_array[:,4]*27.211386245988
    c60000 = data_array[:,5]*27.211386245988
    impot = data_array[:,6]*27.211386245988
    pot.append([Source,z,c150,c600,c2400,c15000,c60000,impot])


fig = plt.figure(figsize=(3.33,3.33))
axs = fig.gca()
i=pot[0]
axs.plot(i[1],i[2],color="blue",markersize=7,linewidth=1.5,marker="o",label=r"$\mathrm{C_{150}}$")
axs.plot(i[1],i[3],color="purple",markersize=7,linewidth=1.5,linestyle='-',marker=10,label=r"$\mathrm{C_{600}}$")
axs.plot(i[1],i[4],color="orange",markersize=7,linewidth=1.5,linestyle='-',marker=11,label=r"$\mathrm{C_{2400}}$")
axs.plot(i[1],i[5],color="red",markersize=7,linewidth=1.5,linestyle='-',marker="+",markeredgewidth=1.5,label=r"$\mathrm{C_{15000}}$")
axs.plot(i[1],i[6],color="lime",markersize=7,linewidth=1.5,linestyle='-',marker="x",markeredgewidth=1.5,label=r"$\mathrm{C_{60000}}$")
axs.plot(i[1],i[7],color="black",markersize=7,linewidth=1.5,linestyle='-',marker="s",markeredgecolor='k',fillstyle='none',markeredgewidth=1.5,label=r"$\mathrm{-6.8028/|}\mathit{z}|$")
axs.text(5.85,-0.15,r"$\mathrm{(a): Q_{mol}=0}$",horizontalalignment='center',verticalalignment='center')
axs.set_xlabel(r"$\mathit{z} \ (a_0)$")  
axs.set_ylabel(r"$\mathit{E}_{pol} \ \mathrm{\left( eV \right)}$")
axs.set_xticks([5,6,7,8,9,10])
axs.set_yticks([-0.1,-0.3,-0.5,-0.7,-0.9,-1.1,-1.3])
axs.xaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.yaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.grid(False)

fig.set_tight_layout(True)
plt.savefig("figure_2_a.png", dpi=300)

pot = []
for filename in sorted(glob.glob("figure_2_b.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    num_rows, num_cols = data_array.shape
    z = data_array[:,0]
    c150 = data_array[:,1]*27.211386245988
    c600 = data_array[:,2]*27.211386245988
    c2400 = data_array[:,3]*27.211386245988
    c15000 = data_array[:,4]*27.211386245988
    c60000 = data_array[:,5]*27.211386245988
    impot = data_array[:,6]*27.211386245988
    pot.append([Source,z,c150,c600,c2400,c15000,c60000,impot])


fig = plt.figure(figsize=(3.33,3.33))
axs = fig.gca()
i=pot[0]
axs.plot(i[1],i[2],color="blue",markersize=7,linewidth=1.5,marker="o",label=r"$\mathrm{C_{150}}$")
axs.plot(i[1],i[3],color="purple",markersize=7,linewidth=1.5,linestyle='-',marker=10,label=r"$\mathrm{C_{600}}$")
axs.plot(i[1],i[4],color="orange",markersize=7,linewidth=1.5,linestyle='-',marker=11,label=r"$\mathrm{C_{2400}}$")
axs.plot(i[1],i[5],color="red",markersize=7,linewidth=1.5,linestyle='-',marker="+",markeredgewidth=1.5,label=r"$\mathrm{C_{15000}}$")
axs.plot(i[1],i[6],color="lime",markersize=7,linewidth=1.5,linestyle='-',marker="x",markeredgewidth=1.5,label=r"$\mathrm{C_{60000}}$")
axs.plot(i[1],i[7],color="black",markersize=7,linewidth=1.5,linestyle='-',marker="s",markeredgecolor='k',fillstyle='none',markeredgewidth=1.5,label=r"$\mathrm{-6.8028/|}\mathit{z}|$")
axs.text(6.05,-0.54,r"$\mathrm{(b): Q_{mol}=+1}$",horizontalalignment='center',verticalalignment='center')
axs.set_xlabel(r"$\mathit{z} \ (a_0)$")
axs.set_ylabel(r"$\mathit{E}_{pol} \ \mathrm{\left( eV \right)}$")
axs.set_xticks([5,6,7,8,9,10])
axs.set_yticks([-0.5,-0.7,-0.9,-1.1,-1.3])
axs.xaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.yaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.grid(False)
axs.legend(loc="lower right", frameon=False, fontsize=8)

fig.set_tight_layout(True)
plt.savefig("figure_2_b.png", dpi=300)
