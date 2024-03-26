from flatspin import * 
import numpy as np 
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors
import sys

plt.figure(dpi=150)
plt.subplot(221)
model = SquareSpinIceClosed()
#model.spin[[0, 4, 39]] = -1 # flip spins 0, 4 and 39

# A spatial vector field defined on a grid
x = np.linspace(0, 2*np.pi, 9, endpoint=True)
y = np.linspace(0, 2*np.pi, 9, endpoint=True)
xx, yy = np.meshgrid(x, y)
print(xx.shape,yy.shape)
H = np.cos(xx) + np.cos(yy)
h_ext = np.stack([0.01*H, 0.1*H], axis=-1)
print(H.shape)
print(f'h_ext.shape: {h_ext.shape}')

model.set_h_ext_grid(h_ext)

plt.subplot(221)
plt.title("H")
plt.imshow(H, cmap='coolwarm_r')
plt.colorbar()

plt.subplot(222)
plt.title("h_ext")
plot_vectors(model.pos, model.h_ext, normalize=True)

h_ext = model.external_fields()

plt.subplot(223)
plt.title("h_par")
quiv = model.plot(C=h_ext[:,0], cmap='coolwarm_r')
plt.colorbar(quiv);

plt.subplot(224)
plt.title("h_perp")
quiv = model.plot(C=h_ext[:,1], cmap='coolwarm_r')
plt.colorbar(quiv);

plt.tight_layout()
plt.show()