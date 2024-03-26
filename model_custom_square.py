from flatspin import CustomSpinIce
from flatspin import SquareSpinIceClosed
import matplotlib.pyplot as plt
import numpy as np
import sys

sq = SquareSpinIceClosed(size=(4,4),init=-1)
print(sq.N)
sq.plot()
plt.show()

sys.exit()

nx = 4
ny = 4
size = (nx,ny)

nrows=2*nx +1
lattice_spacing = 1
a = lattice_spacing

spin_count = nx*(ny+1) + ny*(nx+1)

pos=np.zeros((spin_count,2),dtype=float)
angle=np.zeros(spin_count,dtype=float)

y=0
i=0
for nrow in range(nrows):
    if nrows%2==0: #horz rows
        x=a/2
        ncols=nx
    else: #vert rows
        x=0
        ncols=nx+1

    for ncol in range(ncols):
        pos[i] = [x,y]
        if nrows%2==0:
            
            angle=0

        else:
            
            angle=np.pi/2

        x+=a
        i+=1
    y+=a
print(pos)