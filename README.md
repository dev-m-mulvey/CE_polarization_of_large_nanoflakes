# CE_polarization_of_large_nanoflakes
Repository containing SI for paper titled, "Application of a Charge Equilibration Model to Describe Polarization in Large Polyaromatic Hydrocarbons and Carbon Nanoflakes".

**General note: All directories in the data/ folder will contain the images that appear in the manuscript (.png), the data used to plot them (.out or .csv) in atomic units, and the python scripts used to plot them (.py). The above files will be titled such that they correspond to the image used in the paper.**

## geometries
Contains the geometries of all systems that appear in the paper in atomic units. The geometries are seperated into two folders whose title describe the contents:
* polycyclic_aromatic_hydrocarbons
* carbon_nanoflakes

## data/polarizabilities
Contains the MMA1 model and quantum mechanical (PBE0/MP2 def2-SVPD) in-plane polarizabilities in atomic units that were used to plot figure 1 in the paper. 

## data/polarization_potential
Contains multiple directories which contain the data, plotting scripts, and following images that appear in the paper:
* figure_2: Comparing scaling of grounded and ungrounded MMA1 charge flow polarizartion potential with size of carbon nanoflake
* figure_3: Compares MMA1 and MMA2 model charge flow polarization potentials to the classical image potential
* figure_5: Compares the full (charge flow+inducible dipole) MMA2 model polarization potential to the classical image potential shifted by the image plane
* figure_6: Compares the Coulomb interaction of two negative point charges screened by the MMA2 charge flow model polarization potential and the classical solution for a conducting sheet of infinite extent.

## data/charge_density
Contains two directories with the data (.out), plotting scripts, and images that compare the cumulative charge density from the grounded and ungrounded MMA2 charge flow model to that of the classical solution for a conducting sheet of infinite extent (figure_4 in manuscript).
* h_equals_5: Contains the atomic charges for C60,000 carbon nanoflake when a negative point charge is 5 bohr above the center of the system as described by the MMA2 charge flow model when the nanoflake is grounded (/+1/.out) or ungrounded (/0/.out).  
* h_equals_10: Same as above except it is for the case where the point charge is 10 bohr above the nanoflake.

## Disclaimer
**Beyond what I provide here, if you need information to run the calculations I urge you to read the manual of the programs used. I can't guarantee there is documentation for all the modifications I made and that manuals are completely up to date.**
* [Psi4](https://psicode.org/psi4manual/1.4.0/index.html)
