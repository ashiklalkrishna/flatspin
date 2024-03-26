from flatspin import * 
import numpy as np 
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors
import sys

plt.figure(dpi=150)
plt.subplot(221)
model = SquareSpinIceClosed()
for i in model.indices():
    plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center')
plt.title('Model')
model.plot()
model.spin[[0, 4, 39]] = -1 # flip spins 0, 4 and 39

# Global external field using an array

# A local field which increases in strength with spin index
H = np.linspace(0, 1, model.spin_count)
phi = np.deg2rad(30)
h_ext = np.column_stack([H * np.cos(phi), H * np.sin(phi)])
print(H)
model.set_h_ext(h_ext)

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