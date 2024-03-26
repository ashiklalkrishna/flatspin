import flatspin
import matplotlib.pyplot as plt
import numpy as np

model = flatspin.model.SquareSpinIceClosed()
model.set_temperature(1000)

for i in range(30):
    model.update_thermal_noise()
    model.relax()
model.plot()
plt.show()