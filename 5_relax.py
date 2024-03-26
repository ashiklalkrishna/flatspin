import flatspin
import matplotlib.pyplot as plt
import numpy as np
import sys

model = flatspin.model.SquareSpinIceClosed
model.polarize()
H = 0.1 #0.058

'''# Gradually increase strength of external field in 10 steps
for h in np.linspace(0, H, 10):
    model.set_h_ext([-h, -h])
    model.relax()

plt.figure()
plt.title("After 10 field steps")
model.plot()'''

# Set external field in a single step
model.polarize()
#model.set_h_ext([-H, -H])
E = model.switching_energy()
E_max = np.max(np.abs(E))
plt.figure()
quiv = model.plot(C=E, cmap='coolwarm', clim=(-E_max, E_max))
plt.colorbar(quiv);

model.relax()
plt.figure()
plt.title("After 1 field step")
model.plot();
plt.show()