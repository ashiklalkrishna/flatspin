from flatspin import SpinIce
import numpy as np
import matplotlib.pyplot as plt

class SquareSpinI(SpinIce):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _init_geometry(self):
        nx = self.size[0]   #number of coloums
        ny = self.size[1]   #number of rows

        spin_count = 2 * ((ny + 1) * nx + ny * (nx + 1))

        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        labels = []

        a = self.lattice_spacing
        y = 0
        i = 0

        for row in range(0, 2 * ny + 1):
            is_vert = row % 2 # 1 for vert, 0 for horiz          

            if is_vert==1:
                # vertical row
                x = 0
                ncols = nx+1  
            else:
                # horizontal row
                x = a/2        
                ncols = nx

            for col in range(0, ncols):
                if is_vert==0:  #horizontal spins
                    angle[i] = 0
                    pos[i] = [x, y]
                if is_vert==1:  #vertical spins
                    angle[i] = np.pi/2
                    pos[i] = [x, y]

                label = (row, col)
                labels.append(label)

                x += a
                i += 1

            y += a/2

        self.labels = np.array(labels)
        print(pos)
        return pos, angle


model = SquareSpinI(size=(4,5),use_opencl=True)
model.plot()
plt.show()