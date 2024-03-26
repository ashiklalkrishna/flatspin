import flatspin
import matplotlib.pyplot as plt
import numpy as np

# H decreases linearly from 0.1 to -0.1, then back to 0.1
H = np.linspace(0.1, -0.1, 500)
H = np.concatenate([H, -H])

phi=[0,30,45,60,90]
for i in range(len(phi)):
    phi[i] = np.deg2rad(phi[i])

plt.figure(figsize=(20,10),dpi=200)
plt.subplot(131)
for ph in phi:
    model = flatspin.model.SquareSpinIceClosed()
    h_dir = np.array([np.cos(ph), np.sin(ph)])

    M_H = []

    for h in H:
        model.set_h_ext(h * h_dir)
        model.relax()
        # Magnetization projected along field direction
        m = model.total_magnetization().dot(h_dir)
        M_H.append(m)

    plt.plot(H, M_H, label=f'{np.round(np.rad2deg(ph))}')
plt.title('SquareSpinIceClosed()')
plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)")
plt.legend()

plt.subplot(132)
for ph in phi:
    model = flatspin.model.KagomeSpinIce()
    h_dir = np.array([np.cos(ph), np.sin(ph)])

    M_H = []

    for h in H:
        model.set_h_ext(h * h_dir)
        model.relax()
        # Magnetization projected along field direction
        m = model.total_magnetization().dot(h_dir)
        M_H.append(m)

    plt.plot(H, M_H, label=f'{np.round(np.rad2deg(ph))}')
plt.title('KagomeSpinIce()')
plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)")
plt.legend()

plt.subplot(133)
for ph in phi:
    model = flatspin.model.PinwheelSpinIceLuckyKnot()
    h_dir = np.array([np.cos(ph), np.sin(ph)])

    M_H = []

    for h in H:
        model.set_h_ext(h * h_dir)
        model.relax()
        # Magnetization projected along field direction
        m = model.total_magnetization().dot(h_dir)
        M_H.append(m)

    plt.plot(H, M_H, label=f'{np.round(np.rad2deg(ph))}')
plt.title('PinwheelSpinIceLuckyKnot()')
plt.xlabel("H (mT)")
plt.ylabel(r"M_H (a.u.)")
plt.legend()

plt.savefig(r'D:\Desktop\flatspin_code\hysterisis_sqr_kago_pin.png')
plt.tight_layout()
plt.show()