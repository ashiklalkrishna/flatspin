from flatspin import SpinIce
import numpy as np
import matplotlib.pyplot as plt

class KagomeSpinIce2(SpinIce):
    def _init_geometry(self):
        labels = []

        nx, ny = self.size #number of rings in x and y axis

        n_vert = (nx + 1) * ny 
        '''
        Each ring has 2 vertical spins. Y-axis rings do not share vertical spins. Number of vertical spins along y-axis = number of rings along y-axis = ny.
        In x-axis, two rings share a vert spin. Therefore nx rings share nx-1 vert spins. Plus, we have 2 boundary vert spins. Therefore,Number of vertical spins along x-axis = 2 end spins + nx-1 shared spins = 2+nx-1 = nx+1'''
        n_top_bot = (2 * nx * 2)
        '''Number of horz spins at the top and bottom row = 2 times number of horz rings'''
        n_mid = (2 * nx + 1) * (ny - 1)
        '''Number of horz rings the middle rows = 2 times number of horz rings + 1'''
        spin_count = n_top_bot + n_mid + n_vert

        pos = np.zeros((spin_count, 2), dtype=float)
        angle = np.zeros(spin_count, dtype=float)

        n_rows = 2 * ny + 1 #same as SquareSpinIce
        last_row = n_rows - 1

        a = self.lattice_spacing
        y = 0
        i = 0
        for row in range(0, n_rows):

            if row % 2 == 0: #row=even #"horizontal" magnets (+/-30 degree)

                n_cols = 2 * nx + 1

                if row == 0 or row == last_row:
                    # first and last row has 1 less element
                    n_cols -= 1 #n_cols = 2 * nx 

                x = a/2
                col0 = 0

                #why?
                if ny % 2 == 0 and row == last_row:
                    # even number of magnets, skip first magnet
                    x += 0
                    col0 += 1

                for col in range(col0, col0 + n_cols):
                    pos[i] = [x, y]

                    '''if row % 4 == 0 and col % 2 == 0:   #bottom-even
                        angle[i] = -1*np.deg2rad(30)
                    if row % 4 == 0 and col % 2 == 1:   #bottom-odd
                        angle[i] = 1*np.deg2rad(30)
                    if row % 4 == 2 and col % 2 == 0:   #top-even
                        angle[i] = 1*np.deg2rad(30)
                    if row % 4 == 2 and col % 2 == 1:   #top-odd
                        angle[i] = -1*np.deg2rad(30)'''
                    
                    if row % 4 == 0 and col % 2 == 0:   #bottom-even
                        angle[i] = 1*np.deg2rad(30)
                    if row % 4 == 0 and col % 2 == 1:   #bottom-odd
                        angle[i] = -1*np.deg2rad(70)
                    if row % 4 == 2 and col % 2 == 0:   #top-even
                        angle[i] = -1*np.deg2rad(45)
                    if row % 4 == 2 and col % 2 == 1:   #top-odd
                        angle[i] = 1*np.deg2rad(45)

                    label = (row, col)
                    labels.append(label)

                    x += a
                    i += 1

            else: #row=odd #vertical magnets (90 degrees)
                n_cols = nx + 1

                x = 0   #otherwise ie. belongs to {1,5,9..} 

                if row % 4 == 3: #belongs to {3,7,11..}
                    x += a

                for col in range(0, n_cols):
                    pos[i] = [x, y]
                    angle[i] = np.deg2rad(120)

                    label = (row, col)
                    labels.append(label)

                    x += 2*a #there are two horz spins between each vert spin
                    i += 1

            y += a * np.sqrt(3) / 2

        self.labels = np.array(labels)
        #print(pos)
        return pos, angle
    
model = KagomeSpinIce2(size=(4,5),use_opencl=True)
model.plot()
plt.show()