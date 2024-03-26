from flatspin.model import SquareSpinIceClosed
import matplotlib.pyplot as plt

model = SquareSpinIceClosed()

plt.figure(figsize=(8,4))
plt.subplot(121)
plt.title("Spin indices")
model.plot()
for i in model.indices():
    plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center')

plt.subplot(122)
plt.title("Spin labels")
model.plot()
for i, l in enumerate(model.labels):
    plt.text(model.pos[i,0], model.pos[i,1], tuple(l), ha='center', va='center')
print(model.indices())
plt.show()