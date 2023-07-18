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

#Set of data points used to plot fit and reference image potential
x_dat=np.arange(5,10,0.01)

#Function to fit to MMA model data
def func(x, a):  
    return a/x

#Open csv in current folder, convert to array, and convert data Hartree to eV
for filename in sorted(glob.glob("figure_2_c.csv", recursive=True)):
    Source = os.path.splitext(filename)[0].split(".")[0]
    data = pd.read_csv(filename, sep=",", dtype=np.float64)
    data_array = data.to_numpy()
    z = data_array[:,0]
    MMA1 = data_array[:,1]*27.211386245988
    MMA2 = data_array[:,2]*27.211386245988
    impot = data_array[:,3]*27.211386245988

#Create figure 
fig, axs = plt.subplots(1, 1, figsize=(3.33,3.33))

#Plot the reference image potential curve. 
#Markerstyle is the same as scatter below, but it is scaled down so these points are hidden and the legend still matches
axs.plot(x_dat,-27.211386245988/(4*x_dat),color="black",linestyle='-',markersize=0.01,marker="s",linewidth=2,mfc='none',markeredgewidth=1.5,label=r"$\mathrm{-6.8028/}|\mathit{z}|$")
#Plot the reference image potential data points 5,6,...10
axs.scatter(z,impot,color="black",s=60,facecolors='none',edgecolor='k',linewidth=1.5,marker="s") 

#Fit func() to MMA1 data
popt, pcov = curve_fit(func,z,MMA1) 
#Fit func() to MMA2 data
popt2, pcov2 = curve_fit(func,z,MMA2) 
#Plot the model curves
axs.plot(x_dat,func(x_dat,*popt),color="red",marker='o',markersize=0.01,linewidth=2,linestyle='-',label=r"$\mathrm{{MMA1:}}{:.4f}/|\mathit{{z}}|$".format(popt[0]))
axs.plot(x_dat,func(x_dat,*popt2),color="green",marker='^',markersize=0.01,linewidth=2,linestyle='-',label=r"$\mathrm{{MMA2:}}{:.4f}/|\mathit{{z}}|$".format(popt2[0]))
#Plot the model data points 5,6,...10
axs.scatter(z,MMA1,color="red",s=50,marker="o")
axs.scatter(z,MMA2,color="green",s=50,marker="^")
#Add identifying text
axs.text(6.0,-0.65,r"$\mathrm{(c): Q_{mol}=+1}$",horizontalalignment='center',verticalalignment='center')

#Modify figure to look more like publication's style
axs.set_xlabel(r"$\mathit{z} \ (a_0)$")    
axs.set_xticks([5,6,7,8,9,10])
axs.set_yticks([-0.6,-0.8,-1.0,-1.2,-1.4])
axs.xaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.yaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.grid(False)
#Markerscale for hidden data points that belong to plot rather than scatter
axs.legend(loc="best", frameon=False, markerscale=600, fontsize=9)
axs.set_ylabel(r"$\mathit{E}_{pol} \ \mathrm{\left( eV \right)}$")

fig.set_tight_layout(True)
plt.savefig("figure_2_c.png", dpi=300)
