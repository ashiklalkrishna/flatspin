from flatspin import SquareSpinIceClosed
import matplotlib.pyplot as plt
import numpy as np
plt.figure(dpi=200)
H = np.linspace(0.1, -0.1, 500)
H = np.concatenate([H, -H])

phi = np.deg2rad(45)
h_dir = np.array([np.cos(phi), np.sin(phi)])

for disorder in [0, 0.05, 0.10, 0.25, 0.50]:
    model = SquareSpinIceClosed(disorder=disorder)

    # H, phi and h_dir as before
    M_H = []
    for h in H:
        model.set_h_ext(h * h_dir)
        model.relax()
        m = model.total_magnetization().dot(h_dir)
        M_H.append(m)

    plt.plot(H, M_H, label=f"{disorder * 100}% disorder")

plt.tight_layout()
plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)");
plt.legend()
plt.show()