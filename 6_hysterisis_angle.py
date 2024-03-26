import flatspin
import matplotlib.pyplot as plt
import numpy as np

model = flatspin.model.SquareSpinIceClosed()

# H decreases linearly from 0.1 to -0.1, then back to 0.1
H = np.linspace(0.1, -0.1, 500)
H = np.concatenate([H, -H])

phi=[0,30,45]
for i in range(len(phi)):
    phi[i] = np.deg2rad(phi[i])

for ph in phi:
    h_dir = np.array([np.cos(ph), np.sin(ph)])

    M_H = []

    for h in H:
        model.set_h_ext(h * h_dir)
        model.relax()
        # Magnetization projected along field direction
        m = model.total_magnetization().dot(h_dir)
        M_H.append(m)

    plt.plot(H, M_H, label=f'{np.round(np.rad2deg(ph))}')

plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)")
plt.legend()
plt.show()