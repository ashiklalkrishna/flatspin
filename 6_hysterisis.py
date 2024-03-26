import flatspin
import matplotlib.pyplot as plt
import numpy as np

model = flatspin.model.KagomeSpinIce(size=(10,10))
#model = flatspin.model.KagomeSpinIce()

# H decreases linearly from 0.1 to -0.1, then back to 0.1
H = np.linspace(0.1, -0.1, 500)
H = np.concatenate([H, -H])

#Angle of the external field
phi = np.deg2rad(45)
h_dir = np.array([np.cos(phi), np.sin(phi)])

M_H = []

for h in H:
    model.set_h_ext(h * h_dir)
    model.relax()
    # Magnetization projected along field direction
    m = model.total_magnetization().dot(h_dir)
    M_H.append(m)

plt.plot(H, M_H, label=f'Angle = {round(np.rad2deg(phi))} deg')
plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)")
plt.title('Hysteresis loop of Kagome spin ice')
plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)")
plt.legend()
plt.show()