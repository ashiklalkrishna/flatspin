from flatspin import *
import numpy as np
import matplotlib.pyplot as plt

def neighbors(self, i):
    neighs = self._neighbor_list[i] #self._neighbor_list = self_init_neighbor_list()
    return neighs[neighs >= 0]

def set_neighbor_distance(self, neighbor_distance):
        """ Change the neighbor distance used to calculate dipolar fields """
        self.neighbor_distance = neighbor_distance

        # Invalidate the h_dip cache
        self._h_dip_cache = None

        # Re-initialize neighbor list
        self._neighbor_list = self._init_neighbor_list()
        self.num_neighbors = self._neighbor_list.shape[-1]

        if self.cl:
            self._init_cl_geometry()
        if self.cuda:
            self._init_cuda_geometry()

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

def dipolar_field(self, i):
    """ Calculate total dipolar field parallell to spin i """
    if self.cl:
        # path only for testing
        return self._dipolar_fields_cl()[i]
    if self.cuda:
        return self._h_dip_local_cuda()[i]
    return self._h_dip_local(i)

def _h_dip_local(self, i):
    for jj, j in enumerate(self.neighbors(i)):
        # print("h_dip", jj, j)
        hdip += self._h_dip[i][jj] * self.spin[i] * self.spin[j]
    return self.alpha * hdip

def _h_dip(self):
    if self._h_dip_cache is None:
        self._h_dip_cache = self._init_h_dip()
    return self._h_dip_cache
    
def dipolar_fields(self):
    if self.cl:
        return self._dipolar_fields_cl()

    if self.cuda:
        return self._h_dip_local_cuda()

    h_dip = np.zeros((self.spin_count, 2))

    for i in self.indices():
        h_dip[i] = self.dipolar_field(i)
    return h_dip

model = SquareSpinIceClosed()
model.spin[[0, 4, 39]] = -1 # flip spins 0, 4 and 39

h_dip = model.dipolar_fields()
quiv = model.plot(C=h_dip[:,0], cmap='coolwarm_r')
plt.colorbar(quiv);
plt.show()