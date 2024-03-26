from flatspin import SpinIce
import numpy as np
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors

class ShaktiLattice(SpinIce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _init_geometry(self):
        nx = self.size[0]  # number of untc cells along x-axis
        ny = self.size[1]  # number of unit cells along y-axis

        nx_half = int(nx/2)
        ny_half = int(ny/2)
        base_count = 2 * ( nx * (ny + 1) + (nx + 1) * ny )

        if nx % 2 == 0: #even nx 
            if ny % 2 == 0: #even ny
                internal_count = 2 * (nx * ny) 
            else: #odd ny
                internal_count = 2 * (nx * (ny_half + 1) + nx * ny_half)
        else: #odd nx
            if ny % 2 == 0: #even ny
                internal_count = 2 * (nx_half * ny + (nx_half + 1) * ny)
            else: #odd ny
                internal_count = 2 * ( (nx_half + 1) * (ny_half + 1) + nx_half * ny_half + nx_half * (ny_half + 1) + (nx_half + 1) * ny_half)

        spin_count = base_count + internal_count

        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        labels = []

        a = self.lattice_spacing
        y = 0
        i = 0
        flag=0

        for row in range(0, 4 * ny + 1):
            x = 0
            is_vert = row % 2  # 1 for vert, 0 for horz

            if is_vert == 1: # vertical row
                x=0
                ncols = nx + 1
                if flag==0 or flag==1: #on vert
                    if nx % 2 == 0: #even
                        ncols += nx_half 
                    else:
                        ncols += nx_half + 1
                elif flag==2 or flag==3: #alt vert
                    ncols += nx_half
            
            if is_vert == 0: # horizontal row
                if row % 4 == 0: #base horz
                    x = a/2
                    ncols = 2 * nx  
                elif (row - 6) % 8 == 0: #on horz
                    x = a/2
                    if nx % 2 == 0: #even
                        ncols = 2 * nx_half
                    else:
                        ncols = 2 * (nx_half +1)
                elif (row - 2) % 8 == 0: #alt horz
                    x = 5 * (a/2)
                    ncols = 2 * nx_half
            cflag=0
            for col in range(0, ncols):
                if is_vert==0:  #horizontal spins
                    angle[i] = 0
                    pos[i] = [x, y]
                    if row % 4 == 0:
                        x += a
                    elif ((row - 6) % 8 == 0) or ((row - 2) % 8 == 0):
                        if col % 2 ==0:
                            x += a
                        else:
                            x += 3 * a

                if is_vert==1:  #vertical spins
                    angle[i] = np.pi/2
                    pos[i] = [x, y]
                    if flag==0 or flag==1: #on 
                        if cflag==0 or cflag==1:
                            x += a
                            cflag+=1
                        elif cflag==2:
                            x += 2*a
                            cflag=0
                        
                    elif flag==2 or flag==3: #alt 
                        if cflag==0:
                            x += 2 * a
                            cflag+=1
                        elif cflag==1 or cflag == 2:
                            x += a
                            cflag+=1
                            if cflag==3:
                                cflag=0

                label = (row, col)
                labels.append(label)

                i += 1
            
            y += a / 2

            if is_vert == 1:
                if flag==0 or flag==1:
                    flag+=1
                elif flag==2 or flag==3:
                    flag+=1
                    if flag==4:
                        flag=0

        self.labels = np.array(labels)
        #print(pos)
        return pos, angle
    
plt.figure(dpi=200)
model = ShaktiLattice(size=(3,3), init=1)
#plt.subplot(121)
#model.plot()

#external field
h = 0.1
phi = np.deg2rad(180+15)
h_dir = np.array([np.cos(phi), np.sin(phi)])
model.set_h_ext(h * h_dir)
'''plt.subplot(121)
plot_vectors(model.pos, model.h_ext, normalize=True)
plt.axis(False)'''
model.relax()

#switching energy
E = model.switching_energy()
E_max = np.max(np.abs(E))
plt.subplot(122)
quiv = model.plot(C=E, cmap='coolwarm', clim=(-E_max, E_max))
#plt.colorbar(quiv);
plt.axis(False)

plt.subplot(121)
model.plot()

#plt.savefig(r'D:/Desktop/flatspin_code/1_Model/sw_energy.png')
plt.show()