from flatspin import * 
import numpy as np 
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors
import matplotlib.animation as animation
import sys


model = SquareSpinIceClosed(use_opencl=True)
model.set_temperature(600)

#animation
loop = 30

fig, ax = plt.subplots()
model.update_thermal_noise()
h_therm = model.thermal_fields()
h_therm_magnitude = norm(model.h_therm, axis=-1)
quiv = plot_vectors(model.pos, model.h_therm,
                    C=h_therm_magnitude, cmap='coolwarm', normalize=True)

def update(frame):
    ax.clear()
    #r=np.random.randint(1,100)
    #model.set_random_seed(r)
    model.update_thermal_noise()
    h_therm = model.thermal_fields()
    h_therm_magnitude = norm(model.h_therm, axis=-1)
    quiv = plot_vectors(model.pos, model.h_therm,
                        C=h_therm_magnitude, cmap='coolwarm', normalize=True)
    ax.set_title(f'Frame {frame+1}')

anim = animation.FuncAnimation(fig, update, frames=loop, interval=200, repeat=True)
#anim.save('D:/Desktop/flatspin_code/therm_animation_600.gif', writer='imagemagick')
plt.show()