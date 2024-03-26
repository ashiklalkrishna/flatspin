from flatspin import SpinIce
import numpy as np
import matplotlib.pyplot as plt

class BrickworkSpinIce(SpinIce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _init_geometry(self):
        nx = self.size[0]   #number of coloums
        ny = self.size[1]   #number of rows

        horz_spins = nx * (ny + 1) #number of horizontal spins

        nx_half = int(nx/2)
        ny_half = int(ny/2)

        if nx % 2 == 0: #even nx 
            if ny % 2 == 0: #even ny
                vert_spins = (nx_half+1) * ny_half +  nx_half * ny_half
            else: #odd ny
                vert_spins = (nx_half+1) * (ny_half+1) + nx_half * ny_half
        
        else: #odd nx
            if ny % 2 == 0: #even ny
                vert_spins = (nx_half+1) * ny_half + (nx_half+1) * ny_half
            else: #odd ny
                vert_spins = (nx_half+1) * (ny_half+1) + (nx_half+1) * ny_half
    
        spin_count =  horz_spins + vert_spins
            
        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        labels = []

        a = self.lattice_spacing
        y = 0
        i = 0

        for row in range(0, 2 * ny + 1):  
            is_vert = row % 2 # 1 for vert, 0 for horiz          
            is_on = row % 4 #1 for on, 3 for alt

            if is_vert==0: 
                x = a/2        
                ncols = nx

            if is_vert==1:
                if is_on==1:
                    x = 0
                    ncols =(nx_half + 1)
                if is_on==3:
                    x = 1
                    if nx%2==0:
                        ncols = nx_half
                    else:
                        ncols = (nx_half+1)
                    
            for col in range(0, ncols):
                if is_vert==0:  #horizontal spins
                    angle[i] = 0
                    pos[i] = [x, y]
                    x += a

                if is_vert==1:  #vertical spins
                    angle[i] = np.pi/2
                    pos[i] = [x, y]
                    x += 2 * a

                label = (row, col)
                labels.append(label)
   
                i += 1
            y += a/2

        self.labels = np.array(labels)

        return pos, angle
    
    _vertex_size = (3,2)

model = BrickworkSpinIce(size=(5,7))


'''for i in model.indices():
    plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center')'''
model.plot()
plt.savefig(r'D:/Desktop/flatspin_code/1_Model/brick.png')
plt.show()