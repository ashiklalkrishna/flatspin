import numpy as np
import sys
import matplotlib.pyplot as plt
from flatspin import SquareSpinIceClosed

plt.figure(dpi=200)
for nd in [1, 2]:
    plt.subplot(1,2,nd)
    plt.title(f'neighbor_distance={nd}')
    m = SquareSpinIceClosed(size=(6,6), neighbor_distance=nd)
    i = m.spin_count//2 - 1
    neighs = np.zeros(m.spin_count)
    neighs[i] = 1 #assigning values for colorbar
    neighs[m.neighbors(i)] = 0.8
    m.plot(C=neighs, cmap='coolwarm', clim=(0,1))

plt.show()
