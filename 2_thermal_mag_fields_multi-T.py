from flatspin import * 
import numpy as np 
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors
import matplotlib.animation as animation
import sys


model = SquareSpinIceClosed()
model.set_temperature(600)

loop=3

for i in range (loop):
    plt.subplot(loop, 1, i+1)
    model.update_thermal_noise()
    h_therm = model.thermal_fields()
    h_therm_magnitude = norm(model.h_therm, axis=-1)
    quiv = plot_vectors(model.pos, model.h_therm,
                    C=h_therm_magnitude, cmap='coolwarm', normalize=True)
    #plt.colorbar(quiv)
    #plt.savefig(f'D:/Desktop/flatspin_code/therm_anim/img{i}.png')

plt.show()