
import sys

import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D

import numpy as np
from numpy.random import randn
from scipy import array, newaxis

def open_mom_files(file):

    atoms = []

    with open(file) as f:
        for line in f:
            curr_atom = {}
            label, x, y, z, type_, type_label, rank, rank_no = line.split()

            curr_atom["x"] = float(x)
            curr_atom["y"] = float(y)
            curr_atom["z"] = float(z)
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

atom_info = open_mom_files("./c60000.out")
space_charge_dat = []
for atom in atom_info:
    space_charge_dat.append([atom["x"],atom["y"],atom["z"],atom["charges"][0]])
#Data array containing all copies of ring 
unfiltered_data_array = np.array(space_charge_dat)

# Creating dataset
x = unfiltered_data_array[:,0]
y = unfiltered_data_array[:,1]
z = unfiltered_data_array[:,2]
np.savetxt("C6000.xyz", unfiltered_data_array, fmt="%10.8f")

#z_atoms = np.full(np.shape(z), 0.0000025922)
# 
##fig = plt.figure(figsize=(1.75,1.75))
#fig = plt.figure(figsize=(10,10))
#ax = fig.add_subplot(111, projection='3d', computed_zorder=False)
#
#surf = ax.plot_trisurf(x, y, z, cmap=cm.copper, linewidth=1)
#ax.scatter(x, y, z_atoms, marker='o', s=10, alpha=1, depthshade=False, color='white')
##fig.colorbar(surf)
#ax.scatter(0, 0, 0.045, marker='o', s=100, alpha=1, color='blue')
#
#ax.view_init(elev=50, azim=0, roll=0)
#ax.set_xlim([-100, 100])
#ax.set_ylim([-100, 100])
#ax.set_zlim([0, 0.06])
#ax.set_axis_off()
#
#fig.tight_layout()
#
##plt.show() 
#plt.savefig("test_image.png",dpi=300)
