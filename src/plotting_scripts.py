import numpy as np
import matplotlib.pyplot as plt


import os
from pathlib import Path
import csv
import pandas as pd

PROJ_DIR = Path(__file__).parent.parent

"""
df = pd.read_csv(f'{PROJ_DIR}/data/harmonic_chain_sizes.csv', usecols=[0, 1],header=None)

size = df[0]
time = df[1]

log = np.log(size)

plt.plot(size,time,'.',label="data")
plt.plot(size,log,label="log(size)")
plt.xlabel("system size")
plt.ylabel("scrambling time")
plt.legend()
plt.show()

"""

##########
# BKP vs Gaussian
########

"""
spin_sizes = [3,5,7,9,11]
spin_times = [3,5,7,9,11]


plt.rc('font',size=14)
plt.plot(size[0:7],time[0:7],"ko",label="Gaussian")
plt.plot(spin_sizes,spin_times,'ro',label="BKP")
plt.xlabel("System Size")
plt.ylabel("Evolution Time")
plt.legend()
plt.show()
"""

#########
# mut info vs hole size
#########

"""
hole_size = [0,10,24,33,40,46,52]
mi = [1.26,1.46,1.98,3.76,6.69,7.987,8.1126]

plt.plot(hole_size,mi,'ko')
plt.xlabel("hole size")
plt.ylabel("mutual information")
plt.show()



df_quench = pd.read_csv(f'{PROJ_DIR}/data/vary_quench_time_n_tube_15.csv', usecols=[0, 4],header=None)
quench_times = df_quench[0]
mutual_info = df_quench[1]

plt.plot(quench_times,mutual_info)
plt.xlabel("quench time")
plt.ylabel("mutual information")
"""

"""
df_line = pd.read_csv(f'{PROJ_DIR}/data/hopping_fidelities_line.csv', usecols=[0, 1],header=None)
size_line = df_line[0]
fidelity_line = df_line[1]

df_compare_line = pd.read_csv(f'{PROJ_DIR}/data/hopping_line_compare_fidelities.csv', usecols=[0, 1],header=None)
fidelity_std_line = df_compare_line[1]

plt.rc('font',size=15)
plt.plot(size_line,fidelity_line,'ko',markersize =10,label="many-body")
plt.plot(size_line,fidelity_std_line[0:9],'ro',markersize =10,label="standard")
plt.xlabel("System Size")
plt.ylabel("Fidelity")
plt.legend()
plt.show()

df_ring = pd.read_csv(f'{PROJ_DIR}/data/hopping_fidelities_ring.csv', usecols=[0, 1],header=None)
size_ring = df_ring[0]
fidelity_ring = df_ring[1]

df_compare_ring = pd.read_csv(f'{PROJ_DIR}/data/hopping_ring_compare_fidelities.csv', usecols=[0, 1],header=None)
fidelity_std_ring = df_compare_ring[1]

plt.rc('font',size=15)
plt.plot(size_ring,fidelity_ring,'ko',markersize =10,label="many-body")
plt.plot(size_ring,fidelity_std_ring[0:9],'ro',markersize =10,label="standard")
plt.xlabel("System Size")
plt.ylabel("Fidelity")
plt.legend()
plt.show()


plt.rc('font',size=15)
fig, axs = plt.subplots(1, 2, figsize=(15, 5))
#fig.set_layout_engine('constrained', w_pad=0.5) 
axs[0].plot(size_line,fidelity_line,'ko',markersize =10,label="many-body")
axs[0].plot(size_line,fidelity_std_line[0:9],'ro',markersize =10,label="standard")

axs[0].set_xlabel('System Size')
axs[0].set_ylabel('Fidelity')
axs[0].set_title('No Periodic Boundary Conditions')

axs[1].plot(size_ring,fidelity_ring,'ko',markersize =10,label="many-body")
axs[1].plot(size_ring,fidelity_std_ring[0:9],'ro',markersize =10,label="standard")

axs[1].set_xlabel('System Size')
axs[1].set_ylabel('Fidelity')
axs[1].set_title('Periodic Boundary Conditions')

labels = ["(i)", "(ii)"]

for ax, label in zip(axs.flat, labels):
    ax.text(
        -0.1,  # X-coordinate: slightly to the left of the plot boundary
        1.05,  # Y-coordinate: slightly above the top plot boundary
        label,
        transform=ax.transAxes,  # Use relative axis units (0 to 1)
        fontsize=14,
        fontweight="bold",
        va="bottom",  # Vertical alignment
        ha="right",  # Horizontal alignment
    )
plt.show()
"""


#######
# holes figure
#######


df_0 = pd.read_csv(f'{PROJ_DIR}/data/mi_distrib_0.csv', usecols=[0, 1, 2],header=None)

sites = df_0[0]
left_0 = df_0[1]
right_0 = df_0[2]

df_0_quench = pd.read_csv(f'{PROJ_DIR}/data/mi_distrib_0_quench.csv', usecols=[0, 1],header=None)

time = df_0_quench[0]
ratio_0 = df_0_quench[1]

df_10 = pd.read_csv(f'{PROJ_DIR}/data/mi_distrib_10.csv', usecols=[0, 1, 2],header=None)

left_10 = df_10[1]
right_10 = df_10[2]

df_10_quench = pd.read_csv(f'{PROJ_DIR}/data/mi_distrib_10_quench.csv', usecols=[0, 1],header=None)

ratio_10 = df_10_quench[1]

df_20 = pd.read_csv(f'{PROJ_DIR}/data/mi_distrib_20.csv', usecols=[0, 1, 2],header=None)

left_20 = df_20[1]
right_20 = df_20[2]

df_20_quench = pd.read_csv(f'{PROJ_DIR}/data/mi_distrib_20_quench.csv', usecols=[0, 1],header=None)

ratio_20 = df_20_quench[1]


fig, axs = plt.subplots(2, 3, figsize=(15, 9))
#fig.set_layout_engine('constrained', w_pad=0.5) 
plt.rc('font',size=15)
axs[0,0].plot(sites,left_0,'b',label="left")
axs[0,0].plot(sites,right_0,'r',label="right")

axs[0,0].set_xlabel('Site')
axs[0,0].set_ylabel('Mutual Information')
axs[0,0].set_title("No Hole")

axs[0,1].plot(sites,left_10,'b',label="left")
axs[0,1].plot(sites,right_10,'r',label="right")

axs[0,1].set_xlabel('Site')
axs[0,1].set_ylabel('Mutual Information')
axs[0,1].set_title("Hole Length 10")

axs[0,2].plot(sites,left_20,'b',label="left")
axs[0,2].plot(sites,right_20,'r',label="right")

axs[0,2].set_xlabel('Site')
axs[0,2].set_ylabel('Mutual Information')
axs[0,2].set_title("Hole Length 20")

axs[1,0].plot(time,ratio_0,'k',label="left")

axs[1,0].set_xlabel('Quench Time')
axs[1,0].set_ylabel('Right/Left Mutual Information')

axs[1,1].plot(time,ratio_10,'k',label="left")

axs[1,1].set_xlabel('Quench Time')
axs[1,1].set_ylabel('Right/Left Mutual Information')

axs[1,2].plot(time,ratio_20,'k',label="left")

axs[1,2].set_xlabel('Quench Time')
axs[1,2].set_ylabel('Right/Left Mutual Information')


labels = ["(a)", "(b)", "(c)", None,None,None]


for ax, label in zip(axs.flat, labels):
    ax.text(
        -0.1,  # X-coordinate: slightly to the left of the plot boundary
        1.05,  # Y-coordinate: slightly above the top plot boundary
        label,
        transform=ax.transAxes,  # Use relative axis units (0 to 1)
        fontsize=14,
        fontweight="bold",
        va="bottom",  # Vertical alignment
        ha="right"  # Horizontal alignment
    )
plt.show()



######
# BKP vs Gaussian Oscillating
######
"""
df_bkp = pd.read_csv(f'{PROJ_DIR}/data/fid_vs_coupling_bkp.csv', header=None)
coupling_bkp = df_bkp[0]
fid_bkp = df_bkp[1]

df_harmonic = pd.read_csv(f'{PROJ_DIR}/data/harmonic_mi_vs_coupling.csv', header=None)
coupling_harmonic = df_harmonic[0]
mi_harmonic = df_harmonic[1]

plt.rc('font',size=15)
fig, axs = plt.subplots(1, 2, figsize=(15, 5))

axs[0].plot(coupling_harmonic,mi_harmonic,'k',linewidth =2)

axs[0].set_xlabel('Coupling Time')
axs[0].set_ylabel('Mutual Information')


axs[1].plot(coupling_bkp,fid_bkp,'k',linewidth =2)

axs[1].set_xlabel(r"$g/(2\pi)$")
axs[1].set_ylabel(r"$\langle Z\rangle$")

labels = ["(a)", "(b)"]

for ax, label in zip(axs.flat, labels):
    ax.text(
        -0.1,  # X-coordinate: slightly to the left of the plot boundary
        1.05,  # Y-coordinate: slightly above the top plot boundary
        label,
        transform=ax.transAxes,  # Use relative axis units (0 to 1)
        fontsize=14,
        fontweight="bold",
        va="bottom",  # Vertical alignment
        ha="right",  # Horizontal alignment
    )
plt.show()
"""
print("stop")
