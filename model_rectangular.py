from flatspin import SpinIce
import numpy as np
import matplotlib.pyplot as plt

class RectangularSpinIce(SpinIce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _init_geometry(self):
        nx = self.size[0]   
        ny = self.size[1]   

        spin_count = nx * (ny + 1) + ny * ( int(nx/2) + 1)
            
        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        labels = []

        a = self.lattice_spacing
        y = 0
        i = 0

        for row in range(0, 2 * ny + 1):
            is_vert = row % 2 # 1 for vert, 0 for horiz          

            if is_vert==1:  #vertical row
                x = 0
                ncols = ( int(nx/2) + 1)
                    
            else:   #horizontal row
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

                    x += 2 * a

                label = (row, col)
                labels.append(label)
   
                i += 1
            y += a/2

        self.labels = np.array(labels)

        return pos, angle

#plt.figure(dpi=200)
model = RectangularSpinIce(size=(5,7),use_opencl=True)
#model.flip(6)
model.plot()
plt.savefig(r'D:/Desktop/flatspin_code/1_Model/rect.png')
vert = model.vertices()
print(vert)
model.plot_vertices()
plt.show()