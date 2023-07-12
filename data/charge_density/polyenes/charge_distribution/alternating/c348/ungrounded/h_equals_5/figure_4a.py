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

fig, axs = plt.subplots(figsize=(30,30))

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
        axs.scatter(unfiltered_data_array[:,1],unfiltered_data_array[:,2],c=colors[idx],marker=sty[idx],s=400,label=r"$\mathrm{{MMA2_{{Q_{{mol}}={}}}}}$".format(which_is_it))
axs.set_ylim([-0.0035,0.0035])
axs.grid(False)
axs.xaxis.set_tick_params(direction="in",length=25,width=8)
axs.yaxis.set_tick_params(direction="in",length=25,width=8)
#axs.ticklabel_format(axis='x',style='sci')
plt.ticklabel_format(style='sci', axis='x')
axs.legend(loc='best', frameon=False, title=r"$\mathrm{(a): \ \mathit{h}=5 \ a_{0}}$")
axs.set_xlabel(r"$\mathit{y} \ (a_{0})$")
axs.set_ylabel(r"$\mathit{q} \ (e)$")
plt.savefig("c348_heq5_zoom.png",dpi=300,bbox_inches='tight')
