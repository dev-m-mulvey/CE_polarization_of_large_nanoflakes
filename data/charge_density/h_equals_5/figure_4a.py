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
plt.rcParams.update({'font.size': 50})
rc('font', weight='bold')


def open_mom_files(file):

    atoms = []

    with open(file) as f:
        for line in f:
            curr_atom = {}
            label, x, y, z, type_, type_label, rank, rank_no = line.split()

            curr_atom["x"] = float(x)
            curr_atom["y"] = float(y)
            lines = []
            for i in range(1):
                lines.append(next(f, " ").strip())
            numbers = " ".join(lines)
            numbers = numbers.split()
            numbers = list(map(float, numbers))
            curr_atom["charges"] = []
            # charge
            charge = numbers.pop(0)
            curr_atom["charges"].append(charge)
            atoms.append(curr_atom)
    return atoms

upperdirs = natsort.natsorted(glob.glob("*/", recursive=True),reverse=True)

fig, axs = plt.subplots(figsize=(20,20))

colors=['orange','g','orange','g','y']
line=['-',':','-',':']
sty=['o','o','o','x']
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
        #Calculate distance from origin this will contain duplicates 
        r = np.round(np.linalg.norm(unfiltered_data_array[:,:2], axis=1),6)
        q = np.round(unfiltered_data_array[:,-1],10)
        unique_r, counts_r = np.unique(r, return_counts=True)
        unique_avg_q = []
        sum_at_radius = 0
        for i in range(len(unique_r)):
             charges=q[np.where(r==unique_r[i])[0]]
             num_charges=len(charges)
             a_charge = np.sum(charges)
             sum_at_radius += a_charge
             #avg_charge = a_charge/unique_r[i]
             unique_avg_q.append(sum_at_radius)
        ##Bring together r and charges.
        plot_data = np.vstack((unique_r, unique_avg_q)).T
        axs.scatter(plot_data[:,0],plot_data[:,1],c=colors[idx],marker=sty[idx],s=200,label=r"$\mathrm{{MMA2_{{Q_{{mol}}={}}}}}$".format(which_is_it))
y_classical = []
for i in plot_data[:,0]:
    y_exp = 1-(5/((i**2+25)**float(1/2)))
    y_classical.append(y_exp)
classical_data = np.vstack((unique_r, y_classical)).T
axs.plot(classical_data[:,0],classical_data[:,1],c='k',linewidth=7,label=r"$\mathrm{Conducting \ Sheet}$")
axs.set_xlim([-2,472])
axs.set_ylim([-0.01,1.01])
axs.grid(which='both')
axs.legend(loc=8, frameon=False, title=r"$\mathrm{(a): \ \mathit{h}=5 \ a_{0}}$")
axs.set_xlabel(r"$\mathit{R} \ (a_{0})$")
axs.set_ylabel(r"$q_{Cumulative} \ (e)$")
#axs.text(160,0.27,r"$\mathrm{(a): \ z=5 \ a_{0}}$",horizontalalignment='center',verticalalignment='center',fontsize=45)
plt.savefig("figure_4_a.png",dpi=300,bbox_inches='tight')
