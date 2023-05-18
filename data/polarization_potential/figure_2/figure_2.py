import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob 
import os
from matplotlib import rc
from matplotlib.font_manager import FontProperties


params = {'mathtext.default': 'bf'}
plt.rcParams.update(params)
plt.rcParams.update({'font.size': 55})
rc('font', weight='bold')

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


fig = plt.figure(figsize=(25,25))
axs = fig.gca()
i=pot[0]
axs.plot(i[1],i[2],color="blue",markersize=55,linewidth=5,marker="o",label=r"$\mathrm{C_{150}}$")
axs.plot(i[1],i[3],color="silver",markersize=55,linewidth=5,linestyle='-',marker=10,label=r"$\mathrm{C_{600}}$")
axs.plot(i[1],i[4],color="green",markersize=55,linewidth=5,linestyle='-',marker=11,label=r"$\mathrm{C_{2400}}$")
axs.plot(i[1],i[5],color="orange",markersize=55,linewidth=5,linestyle='-',marker="X",label=r"$\mathrm{C_{15000}}$")
axs.plot(i[1],i[6],color="red",markersize=55,linewidth=5,linestyle='-',marker="P",label=r"$\mathrm{C_{60000}}$")
axs.plot(i[1],i[7],color="black",markersize=55,linewidth=5,linestyle='-',marker="o",label=r"$\mathrm{-6.8028/z}$")
axs.text(5.6,-0.15,r"$\mathrm{(a): Q_{mol}=0}$",horizontalalignment='center',verticalalignment='center',fontsize=70)
axs.set_xlabel(r"$z \ a_0$")    
axs.set_xticks([5,6,7,8,9,10])
axs.grid(which='major', linestyle='-')
axs.legend(loc="best", frameon=False, fontsize='large')
axs.set_ylabel(r"$\mathrm{V} \ \mathrm{\left( eV \right)}$")

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


fig = plt.figure(figsize=(25,25))
axs = fig.gca()
i=pot[0]
axs.plot(i[1],i[2],color="blue",markersize=55,linewidth=5,marker="o",label=r"$\mathrm{C_{150}}$")
axs.plot(i[1],i[3],color="silver",markersize=65,linewidth=5,linestyle='-',marker=10,label=r"$\mathrm{C_{600}}$")
axs.plot(i[1],i[4],color="green",markersize=55,linewidth=5,linestyle='-',marker=11,label=r"$\mathrm{C_{2400}}$")
axs.plot(i[1],i[5],color="orange",markersize=45,linewidth=5,linestyle='-',marker="X",label=r"$\mathrm{C_{15000}}$")
axs.plot(i[1],i[6],color="red",markersize=45,linewidth=5,linestyle='-',marker="P",label=r"$\mathrm{C_{60000}}$")
axs.plot(i[1],i[7],color="black",markersize=55,linewidth=5,linestyle='-',marker="o",label=r"$\mathrm{-6.8028/z}$")
axs.text(5.75,-0.55,r"$\mathrm{(b): Q_{mol}=+1}$",horizontalalignment='center',verticalalignment='center',fontsize=70)
axs.set_xlabel(r"$z \ a_0$")    
axs.set_xticks([5,6,7,8,9,10])
axs.grid(which='major', linestyle='-')
axs.legend(loc="lower right", frameon=False, fontsize='large')
axs.set_ylabel(r"$\mathrm{V} \ \mathrm{\left( eV \right)}$")

fig.set_tight_layout(True)
plt.savefig("figure_2_b.png", dpi=300)
