from flatspin import SquareSpinIceClosed
import matplotlib.pyplot as plt
import numpy as np

H = np.linspace(0.1, -0.1, 500)
H = np.concatenate([H, -H])

phi = np.deg2rad(45)
h_dir = np.array([np.cos(phi), np.sin(phi)])

model = SquareSpinIceClosed(m_therm=.5e-17) #m_therm = thermal nucleation moment

temperatures = [100,300,600,1000]

for T in temperatures:
    M_H = []

    model.polarize()
    model.set_temperature(T)
    for h in H:
        model.set_h_ext(h * h_dir)
        model.relax()
        m = model.total_magnetization().dot(h_dir)
        M_H.append(m)

    plt.plot(H, M_H, label=f"{T}K")

plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)");
plt.legend();
plt.show()