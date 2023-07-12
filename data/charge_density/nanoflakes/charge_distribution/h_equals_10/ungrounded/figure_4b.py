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
rc('axes',linewidth=5,edgecolor='k')

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

        negative_x_loc = np.where(np.sign(unfiltered_data_array[:,0])<0)[0]
        negative_x_array = unfiltered_data_array[negative_x_loc,:]
        r_negative = np.linalg.norm(negative_x_array[:,:2], axis=1)
        print(len(r_negative))
        unique_r_neg, counts_r_neg = np.unique(r_negative, return_counts=True)
        unique_avg_q_neg = []
        sum_neg_charges=0
        for i in range(len(unique_r_neg)):
             charges=negative_x_array[np.where(r_negative==unique_r_neg[i])[0],2]
             if np.all(charges*charges[0]<0):
                 print("charges of differing sign found within same radius")
             #else:
             #    print("All charges the same")
             num_charges=len(charges)
             sum_neg_charges += num_charges
             a_charge = np.sum(charges)
             avg_charge = a_charge/num_charges
             unique_avg_q_neg.append(avg_charge)
        q_neg = np.array(unique_avg_q_neg)

        positive_x_loc = np.where(np.sign(unfiltered_data_array[:,0])>0)[0]
        positive_x_array = unfiltered_data_array[positive_x_loc,:]
        r_positive = np.linalg.norm(positive_x_array[:,:2], axis=1)
        print(len(r_positive))
        unique_r_pos, counts_r_pos = np.unique(r_positive, return_counts=True)
        unique_avg_q_pos = []
        sum_pos_charges=0
        for i in range(len(unique_r_pos)):
             charges=positive_x_array[np.where(r_positive==unique_r_pos[i])[0],2]
             if np.all(charges*charges[0]<0):
                 print("charges of differing sign found within same radius")
             #else:
             #    print("All charges the same")
             num_charges=len(charges)
             sum_pos_charges += num_charges
             a_charge = np.sum(charges)
             avg_charge = a_charge/num_charges
             unique_avg_q_pos.append(avg_charge)
        q_pos =np.array(unique_avg_q_pos)

print(np.shape(unique_r_neg))
print(np.shape(unique_r_pos))

axs.scatter(unique_r_pos,q_pos,c="orange",marker="o",s=400,label=r"$MMA2_{Q_{mol}=0}$")
axs.scatter(-1.0*unique_r_neg,q_neg,c="orange",marker="o",s=400)
axs.set_ylim([-0.0002,0.0002])
axs.grid(False)
axs.xaxis.set_tick_params(direction="in",length=25,width=8)
axs.yaxis.set_tick_params(direction="in",length=25,width=8)
axs.legend(loc='best', frameon=False, title=r"$\mathrm{(a): \ \mathit{h}=10 \ a_{0}}$",fontsize='40')
axs.set_xlabel(r"$\mathit{r \cdot sgn(x)} \ (a_{0})$")
axs.set_ylabel(r"$\mathit{q} \ (e)$")
plt.savefig("c60k_heq10_zoom.png",dpi=300,bbox_inches='tight')