from flatspin import SpinIce
import numpy as np
import matplotlib.pyplot as plt
import time
st=time.time()

class SquareSpinIceClosed(SpinIce):
    def __init__(self, *, edge="symmetric", **kwargs):
        assert edge in ("symmetric", "asymmetric")
        self.edge = edge

        super().__init__(**kwargs)

    def _init_geometry(self):
        nx, ny = self.size     #number spins along x and y axis
        '''#same as nx,ny above
        nx = self.size[0]   #number of coloums
        ny = self.size[1]   #number of rows'''

        sym = 1 if self.edge == "symmetric" else 0  #number of spins
        spin_count = (ny + sym) * nx + ny * (nx + sym) 
        '''#same as spin_count above
        if self.edge=='asymmetric': 
            spin_count = 2*nx*ny
        else:
            spin_count = 2*nx*ny + (nx+ny)'''
            
        pos = np.zeros((spin_count, 2), dtype=float)    
        #postion matrix is a 2d matric of spin_count number of 2-tuple elements denoting the coordinates of spin_count number of spins
        angle = np.zeros(spin_count, dtype=float)
        #angle matrix is a 1d matric of spin_count number of elements denoting the angles of spin_count number of spins

        labels = []

        a = self.lattice_spacing
        y = 0
        i = 0

        for row in range(0, 2 * ny + sym): 
            #number of rows = 2*number of spins along y axis + sym (1 extra row of horz spins at the top for symmetric). range() goes from 0 to n-1

            is_vert = row % 2 # 1 for vert, 0 for horiz
            ncols=nx #both horz and vert coloums have at least nx coloumns
            x=0

            if is_vert==1:
                # vertical row
                ncols += sym #first vertical col begins at x=0
            else:
                # horizontal row
                x += a/2   #first horz col begins at x=a/2

            '''#or assign ncols=nx+sym for vert and ncols=nx for horz coloums
            if is_vert==1:      # vertical row
                x = 0
                ncols = nx+sym   
            else:               #horizontal row
                x = a/2        
                ncols = nx'''   

            for col in range(0, ncols):
                if is_vert:
                    angle[i] = np.pi/2  #vertical spins have 90 angle
                pos[i] = [x, y]         #y is initialised to 0

                label = (row, col)
                labels.append(label)

                x += a      #each col is seperated by 'a' distance
                i += 1      #next spin i.e element in the pos[] and angle[]

                '''#mentioning pos and angle of vertical and horz spins explicitly

                for col in range(0, ncols):
                if is_vert==0:  #horizontal spins
                    angle[i] = 0
                    pos[i] = [x, y]
                if is_vert==1:  #vertical spins
                    angle[i] = np.pi/2
                    pos[i] = [x, y]

                label = (row, col)
                labels.append(label)
                '''
            y += a/2 
            #each row is seperated  by 'a/2'. Note that hor and vert spins form seperate rows. Distance between two horz(vert) rows is 'a'

        self.labels = np.array(labels)
        return pos, angle

model = SquareSpinIceClosed(init='ground',use_cuda=True)
#print(model.pos)
model.plot()
plt.show()

et=time.time()
ft=et-st
print(f'Time={ft:.5f}s')

