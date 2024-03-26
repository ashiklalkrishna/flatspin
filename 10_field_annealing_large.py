from flatspin.model import SquareSpinIceClosed
from flatspin.model import KagomeSpinIce
from flatspin.encoder import Rotate
import matplotlib.pyplot as plt
import numpy as np

model = SquareSpinIceClosed(size=(10,10), init='polarize', disorder=0.05)

timesteps = 64
enc_rotate = Rotate(H=0.09, H0=0.06, timesteps=timesteps)
input = np.linspace(1, 0, 20)

h_ext = enc_rotate(input)
H = np.linalg.norm(h_ext, axis=1)

spins = []
flips = []
E_dip = []
for i, h in enumerate(h_ext):
    model.set_h_ext(h)
    s = model.relax()
    if (i+1) % timesteps == 0:
        # Record spin state at the end of each rotation
        spins.append(model.spin.copy())
    flips.append(s)
    E_dip.append(model.total_dipolar_energy())

plt.plot(E_dip)
plt.ylabel("Energy")
plt.xlabel("Time");
plt.show()