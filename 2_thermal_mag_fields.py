from flatspin import * 
import numpy as np 
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors
import sys

plt.figure(dpi=150)
plt.subplot(221)
model = KagomeSpinIce()
for i in model.indices():
    plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center')
plt.title('Model')
model.spin[[0, 4, 39]] = -1 # flip spins 0, 4 and 39
model.plot()

model.set_temperature(600)
model.update_thermal_noise()

plt.subplot(222)
plt.title("h_therm @ 600 K")
h_therm_magnitude = norm(model.h_therm, axis=-1)
h_therm = model.thermal_fields()
# Colorize vectors by their magnitude
quiv = plot_vectors(model.pos, model.h_therm,
                    C=h_therm_magnitude, cmap='coolwarm', normalize=True)

plt.subplot(223)
plt.title('h_par')
quiv2 = model.plot(C=h_therm[:,0], cmap='coolwarm', normalize=True)
plt.colorbar(quiv2);

plt.subplot(224)
plt.title('h_perp')
quiv3 = model.plot(C=h_therm[:,1], cmap='coolwarm', normalize=True)
plt.colorbar(quiv3);

plt.tight_layout()
plt.show()