from flatspin.model import CustomSpinIce
import numpy as np
import matplotlib.pyplot as plt

# Size (cols, rows) of our geometry
size = (4, 15)

# Positions of spins
lattice_spacing = 1
x = lattice_spacing * np.arange(0, size[0])
y = lattice_spacing * np.arange(0, size[1])
print(x,'\n',y)
xx, yy = np.meshgrid(x, y)
print('\n\n',xx,'\n\n',yy)
xx = xx.ravel()
yy = yy.ravel()
print('\n\n',xx,'\n\n',yy)
pos = np.column_stack([xx, yy])
print('\n\n',pos)

# Angles of spins
delta_angle = 10
angle = (xx+yy) * delta_angle / lattice_spacing

# Create coordinate vectors
x = np.arange(-5, 6, 1)
y = np.arange(-3, 4, 1)

# Create a meshgrid from the coordinate vectors
X, Y = np.meshgrid(x, y)

# Display the coordinates
print("X coordinates:\n", X)
print("Y coordinates:\n", Y)

# Plot the meshgrid points
plt.scatter(X, Y, color='red')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Meshgrid Example')
plt.grid(True)
plt.show()

# Give the angles and positions to CustomSpinIce
'''model = CustomSpinIce(magnet_coords=pos, magnet_angles=angle, radians=False)
model.plot();
plt.show()'''