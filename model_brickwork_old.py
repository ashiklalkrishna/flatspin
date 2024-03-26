from flatspin import SpinIce
import numpy as np
import matplotlib.pyplot as plt

class BrickworkSpinIce(SpinIce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _init_geometry(self):
        nx = self.size[0]   #number of coloums
        ny = self.size[1]   #number of rows

        horz_count = nx*(ny+1)
        vert_count=0

        for n in (range(1,ny+1)):
            if n%2!=0:
                if nx%2==0: #even
                    vert_count += (int(np.ceil(nx/2))+1)
                else:  #odd
                    vert_count += (ny/2)
            else:
                vert_count += int(np.ceil(nx/2))

        spin_count = horz_count + vert_count
            
        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        labels = []

        a = self.lattice_spacing
        y = 0
        i = 0

        for row in range(0, 2*ny+1):  
            is_vert = row % 2 # 1 for vert, 0 for horiz          
            
            if is_vert==1: 
                x = a   #alt
                ncols = int(np.ceil(nx/2))

                if row % 4 == 1:    #on    
                    x = 0
                    if nx%2==0: #even
                        ncols = (int(np.ceil(nx/2))+1)
                    else: #odd
                        ncols = (int(np.ceil(nx/2)))

                '''elif row % 4 == 3:  #alt
                    x = a
                    ncols = int(np.ceil(nx/2))'''

            if is_vert==0:
                # horizontal row
                x = a/2        
                ncols = nx

            for col in range(0, ncols):
                if is_vert==0:  #horizontal spins
                    angle[i] = 0
                    pos[i] = [x, y]
                    x += a

                if is_vert==1:  #vertical spins
                    angle[i] = np.pi/2
                    pos[i] = [x, y]
                    x += 2*a

                label = (row, col)
                labels.append(label)
   
                i += 1

            y += a/2

        self.labels = np.array(labels)
        print(pos)
        return pos, angle


model = BrickworkSpinIce(size=(6,3),use_cuda=True)
model.plot()
print(model.N)
plt.grid()
plt.show()