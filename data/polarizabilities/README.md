## Description of polarizability calculations
We employed the finite field method to calculate the PBE0 and MP2 polarizabilities that appear in the paper.
We used a 3-point forward finite difference formula of the induced dipole:

```math
\alpha_{ii} = {\mu(0) + 4\mu(E^{i}_{h}) - \mu(E^{i}_{2h}) \over 2h} 
```

where $\alpha_{ii}$ is the static dipole polarizability entry with cartesian component $i$, $\mu$ is the induced dipole, $E^{i}$ is a uniform electric field in direction $i$, and $h$ is the strength of the applied electric field. 
Note that the first entry ($\mu (0)$) is the permanent dipole, which is zero for the hexagonal PAHs we cosider, so that term drops out of the above equation. 

The strength of the applied field ($h$) was adjusted with the size of PAH to avoid overpolarizing and introducing contamination by higher order polarizabilities/hyperpolarizabilities.
We used a simple criterion to evaluate if the above condition was met: If doubling $h$ corresponded to a doubling of $\alpha_{ii}$, as the latter should increase linearly with field strength so long as other polarizabilities are not contaminating its measurement.
We list the value of $h$ used for each PAH below in atomic units:
* C6H6: 0.00025
* C24H12: 0.00025
* C54H18: 0.00025
* C96H24: 0.000125
* C150H30: 0.0001
* C216H36: 0.0001
* C294H42: 0.00005
* C384H48: 0.00005

The calcultions were performed using the density fitted restricted Kohn-Sham (DF-KS) and frozen core MP2 modules (DF-MP2) in Psi4 with the standard convergence criteria. 
As described in the manuscript, we used a trimmed version of def2-SVPD as our main orbital basis (which is available in this same directory in Psi4 formatting).
We used the def2-universal-jkfit density fitting basis to fit the Coulomb and exchange integrals of the DFT calculations and those of the HF trial for the MP2 calculations.
For density fitting the integral transformations that happen in MP2, the def2-svpd-ri basis was used.
The properties() module of Psi4 was used to obtain the induced dipoles (which guarantees the relaxed density was used in MP2).


## Disclaimer
**Beyond what I provide here, if you need information to run the calculations I urge you to read the manual of the programs used. I can't guarantee there is documentation for all the modifications I made and that manuals are completely up to date.**
* [Psi4](https://psicode.org/psi4manual/1.4.0/index.html)
