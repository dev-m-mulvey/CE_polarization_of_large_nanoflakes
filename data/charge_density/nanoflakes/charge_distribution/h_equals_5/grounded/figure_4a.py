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

        negative_x_loc = np.where(np.sign(unfiltered_data_array[:,0])<0)[0]
        negative_x_array = unfiltered_data_array[negative_x_loc,:]
        r_negative = np.round(np.linalg.norm(negative_x_array[:,:2], axis=1),6)
        unique_r_neg, counts_r_neg = np.unique(r_negative, return_counts=True)
        unique_avg_q_neg = []
        for i in range(len(unique_r_neg)):
             charges=negative_x_array[np.where(r_negative==unique_r_neg[i])[0],2]
             num_charges=len(charges)
             a_charge = np.sum(charges)
             avg_charge = a_charge/num_charges
             unique_avg_q_neg.append(avg_charge)

        positive_x_loc = np.where(np.sign(unfiltered_data_array[:,0])>0)[0]
        positive_x_array = unfiltered_data_array[positive_x_loc,:]
        r_positive = np.linalg.norm(positive_x_array[:,:2], axis=1)
        unique_r_pos, counts_r_pos = np.unique(r_positive, return_counts=True)
        unique_avg_q_pos = []
        for i in range(len(unique_r_pos)):
             charges=positive_x_array[np.where(r_positive==unique_r_pos[i])[0],2]
             num_charges=len(charges)
             a_charge = np.sum(charges)
             avg_charge = a_charge/num_charges
             unique_avg_q_pos.append(avg_charge)

#Now that are split up check if the averages make sense and they are grouped such that exent along x-axis is defining feature. If so plot them individually, just use the same style of data points. 


        for i in negative_x_loc:
                    r = np.round(np.linalg.norm(unfiltered_data_array[:,:2], axis=1),6)

        #    r = np.round(np.linalg.norm(unfiltered_data_array[:,:2], axis=1),6)

        #x = unfiltered_data_array[only_x_loc,0][0]
        #q = unfiltered_data_array[only_x_loc,2][0]
        #axs.scatter(x,q,c=colors[idx],marker=sty[idx],s=400,label=r"$\mathrm{{MMA2_{{Q_{{mol}}={}}}}}$".format(which_is_it))
##axs.set_xlim([-1,472])
##axs.set_ylim([0,0.00001])
#axs.grid(False)
#axs.xaxis.set_tick_params(direction="in",length=25,width=8)
#axs.yaxis.set_tick_params(direction="in",length=25,width=8)
##axs.set_xticks([100,200,300,400])
#axs.legend(loc='best', frameon=False, title=r"$\mathrm{(a): \ \mathit{h}=5 \ a_{0}}$",fontsize='40')
#axs.set_xlabel(r"$\mathit{x} \ (a_{0})$")
#axs.set_ylabel(r"$\mathit{q} \ (e)$")
#plt.savefig("charge_dist_heq5_c60k_reference.png",dpi=300,bbox_inches='tight')