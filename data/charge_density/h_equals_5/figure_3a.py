import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc
import glob 
import os
import natsort
from scipy.optimize import curve_fit
from collections import Counter

params = {'mathtext.default': 'bf'}
plt.rcParams.update(params)
plt.rcParams.update({'font.size': 10})
rc('font', family='Nimbus Sans', weight='bold')
rc('axes',linewidth=1,edgecolor='k')

#Function that reads a moments file and converts it into an array
def open_mom_files(file):
    #Array containing all coordinates and charges
    atoms = []

    #Loop over lines in moments file
    with open(file) as f:
        for line in f:
            #Dictionary 
            curr_atom = {}
            #Items on a on a line
            label, x, y, z, type_, type_label, rank, rank_no = line.split()
            #Store items in dictionary
            curr_atom["x"] = float(x)
            curr_atom["y"] = float(y)
            lines = []
            for i in range(1):
                lines.append(next(f, " ").strip())
            numbers = " ".join(lines)
            numbers = numbers.split()
            numbers = list(map(float, numbers))
            curr_atom["charges"] = []
            #Charges
            charge = numbers.pop(0)
            curr_atom["charges"].append(charge)
            #Append current dictionary for atom to the list of atom info
            atoms.append(curr_atom)
    return atoms

upperdirs = natsort.natsorted(glob.glob("*/", recursive=True),reverse=True)

#Create figure 
fig, axs = plt.subplots(figsize=(3.33,3.33))

colors=['orange','g']
sty=['o','^']
fccolor=['orange','none']
#Open csv's in all subfolders and convert to array
for idx,direct in enumerate(upperdirs):
    for filename in sorted(glob.glob("{}*.out".format(direct), recursive=True)):
        Source = os.path.splitext(filename)[0].split("/")
        which_is_it = Source[0]
        atom_info = open_mom_files(filename)
        space_charge_dat = []
        for atom in atom_info:
            space_charge_dat.append([atom["x"],atom["y"],atom["charges"][0]])
        #Data array containing all copies of ring 
        unfiltered_data_array = np.array(space_charge_dat)
        #Calculate distance of every charge from origin this will contain duplicates 
        r = np.round(np.linalg.norm(unfiltered_data_array[:,:2], axis=1),6)
        #Charges 
        q = np.round(unfiltered_data_array[:,-1],10)
        #Extract unique values of radii
        unique_r, counts_r = np.unique(r, return_counts=True)
        #Array to store charges that correspond to unique radii
        unique_avg_q = []
        #Sum of all charges at a radius 
        sum_at_radius = 0
        #Loop over the unique radii
        for i in range(len(unique_r)):
             #Find all charges that have the current unique radius
             charges=q[np.where(r==unique_r[i])[0]]
             #Number of charges with radius
             num_charges=len(charges)
             #Sum of those charges
             a_charge = np.sum(charges)
             #Sum of all atomic charges within given radius, should accumulate to 0 or +1 at end
             sum_at_radius += a_charge
             #Current value of charge contained within radius
             unique_avg_q.append(sum_at_radius)
        #print(sum_at_radius)
        #Bring together r and charges
        plot_data = np.vstack((unique_r, unique_avg_q)).T
        #Plot the cumulative charge as a function of radius
        axs.scatter(plot_data[:,0],plot_data[:,1],color=colors[idx],facecolors=fccolor[idx],marker=sty[idx],s=15,label=r"$\mathrm{{MMA2_{{Q_{{mol}}={}}}}}$".format(which_is_it))

#Array for the cumulative induced charge from classical continuum image potential model
y_classical = []
#Calculate the cumulative induced charge for radius (i) for a point charge at 5
for i in plot_data[:,0]:
    y_exp = 1-(5/((i**2+25)**float(1/2)))
    y_classical.append(y_exp)

#Bring together r and charges
classical_data = np.vstack((unique_r, y_classical)).T
#Plot the reference cumulative charge as a function of radius
axs.plot(classical_data[:,0],classical_data[:,1],c='k',linewidth=1.5,label=r"$\mathrm{Conducting \ Sheet}$")

#Modify figure to look more like publication's style
axs.set_xlim([-5,476])
axs.set_ylim([-0.05,1.05])
axs.grid(False)
axs.xaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.yaxis.set_tick_params(direction="in",length=3,width=1,pad=6.25)
axs.set_xticks([100,200,300,400])
axs.legend(loc=8, frameon=False, markerscale=1.5, title=r"$\mathrm{(a): \ \mathit{z}=5 \ a_{0}}$")
axs.set_xlabel(r"$\mathit{R} \ (a_{0})$")
axs.set_ylabel(r"$\mathit{q}_{Cumulative} \ (e)$")

fig.set_tight_layout(True)
plt.savefig("figure_3_a.png",dpi=300)
