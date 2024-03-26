from flatspin import * 
import numpy as np 
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors
import sys

'''
def spin_dipolar_field(self, i, j):
    """ Calculate dipolar field between spin i and j relative to positive spin """
    r = self.pos[j] - self.pos[i]
    dist = np.linalg.norm(r)
    mi = self.m[i]  #self.m = np.column_stack([np.cos(self.angle), np.sin(self.angle)])
    mi_perp = [-mi[1], mi[0]]
    mj = self.m[j]
    h_dip_1 = -mj / dist**3
    h_dip_2 = 3 * r * mj.dot(r) / dist**5
    #h_dip_2 = 3 * r * np.dot(mj,r) / dist**5
    h_dip = h_dip_1 + h_dip_2

    h_par = np.dot(h_dip, mi)
    h_perp = np.dot(h_dip, mi_perp)
    
    return np.array([h_par, h_perp], dtype=float)
'''

'''
model = IsingSpinIce(size=(1,2))
print(model.pos[0],model.pos[1])
print(model.vectors[0],model.vectors[1])

model.plot()

for i in model.indices():
    plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center')

h_dip = model.spin_dipolar_field(0,1)
print(h_dip)

quiv = model.plot(C=h_dip[1], cmap='coolwarm_r')
plt.colorbar(quiv);
plt.show()
'''

'''class MySpinIce(SpinIce):
    def __init__(self, **kwargs):

        super().__init__(**kwargs)

    def _init_geometry(self):

        spin_count = 2
        
        pos = np.zeros((spin_count, 2), dtype=float)  
        angle = np.zeros(spin_count, dtype=float)

        pos[0] = (1.0, 1.0)
        pos[1] = (0.5, 1.5)
        angle[0] = np.deg2rad(0)
        angle[1] = np.deg2rad(90)

        return pos, angle
model=MySpinIce()
h_ind_dip = model.spin_dipolar_field(0,1)
print(h_ind_dip)
model.plot()
plt.show()'''

model = SquareSpinIceClosed(neighbor_distance=1,alpha=1)

h_ind_dip = model.spin_dipolar_field(0,1)
h_dip = model.dipolar_fields()
print(h_dip)

plt.figure(dpi=200)
plt.subplot(121)
quiv = model.plot(C=h_dip[:,0], cmap='coolwarm_r')
plt.title('h_par')
#for i in model.indices():
 #   plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center',)
plt.colorbar(quiv);
plt.subplot(122)
quiv = model.plot(C=h_dip[:,1], cmap='coolwarm_r')
plt.title('h_perp')
plt.colorbar(quiv);
plt.tight_layout()
#plt.savefig(r'D:\Desktop\flatspin_code\kagome_dip_fields.png')
plt.show()