import flatspin
import matplotlib.pyplot as plt 
import numpy as np

#for SquareSpinIceClosed, the size  specifies the number of columns (rows) of horizontal (vertical) magnets. For KagomeSpinIce, the size denotes the number of hexagonal units.

# Model parameters:class flatspin.model.SpinIce(*, size=(4, 4), lattice_spacing=1, hc=0.2, alpha=0.001, disorder=0, h_ext=(0, 0), neighbor_distance=1, switching='sw', sw_b=0.41, sw_c=1, sw_beta=1.5, sw_gamma=3.9, temperature=0, therm_timescale=1, m_therm=7.567999999999999e-17, attempt_freq=1000000000.0, flip_mode='max', init='polarized', spin_axis=None, random_prob=0.5, random_seed=0, use_opencl=False, opencl_platform=0, opencl_device=0, use_cuda=False, astroid_resolution=1801)

model = flatspin.model.SquareSpinIceClosed(size=(20,20),init='random')
#plt.savefig(r'D:\Desktop\flatspin_code\1_Model\square.png')
plt.show()
'''
#spin labels
for i in model.indices():
    plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center
'''

'''
#SPIN
print(model.spin)

print(model.spin_count)
print(model.N)
print(model.label)
print(model.indexof((1,5)))

#Label
L = model.L 
print("(4,2):", L[4,2])
print("Row 3:", L[3])
print("Column 4:", L[:,4])
print("Rows 1-3:", L[1:4])
print("Odd rows:", L[1::2])

print(model.width, model.height)
print(model.spin)
model.spin[4] = -1
model.spin[-3] = -1
model.flip(6)
'''

'''
#Spin ice geometry is defined by the positions and angles of all the spins, and are stored in the pos and angle attributes. Positions are in reduced units, defined by alpha. The angles are in radians and define the rotation for the spins assuming a positive spin value of 1. These attributes are considered read-only and cannot be changed after model initialization.

print(f"Spin 0 has position {model.pos[0]} and angle {np.rad2deg(model.angle[0])}")
print(f"Spin 4 has position {model.pos[4]} and angle {np.rad2deg(model.angle[4])}")

print(model.pos)
print(model.angle)
print(np.rad2deg(model.angle))

print(model.spin)
model.set_spin([1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1])
print(model.spin)

model.set_pos(
[[0.5, 0. ],
 [1.5, 0.5 ],
 [0.  ,0.5],
 [1.  ,0.5],
 [2.  ,0.5],
 [0.5 ,1. ],
 [1.5 ,1. ],
 [0.  ,1.5],
 [1.  ,1.5],
 [2.  ,1.5],
 [0.5 ,2. ],
 [1.5 ,2. ]])

model.set_angle([0., 0., 1.57079633, 1.57079633, 1.57079633, 0., 0., 1.57079633, 1.57079633, 1.57079633, 0., 0.])

model.set_geometry([[0.5, 0. ],
 [1.5, 0.5 ],
 [0.  ,0.5],
 [1.  ,0.5],
 [2.  ,0.5],
 [0.5 ,1. ],
 [1.5 ,1. ],
 [0.  ,1.5],
 [1.  ,1.5],
 [2.  ,1.5],
 [0.5 ,1.5 ],
 [1.5 ,2. ]], [0., 0., 1.57079633, 1.57079633, 1.57079633, 0., 0., 1.57079633, 1.57079633, 1.57079633, 0., 0.])

model.plot();
plt.show()'''

'''
#set spin from image
model.set_spin_image('D:\Desktop\Artificial Spin Ice\shakti_image.jpg')
model.plot()
plt.show()
'''

#Change lattice spacing
#model2 = flatspin.model.SquareSpinIceClosed(lattice_spacing=10)

'''
#Magnetization

#angle is independent of the current spin state. To obtain the magnetization direction, use vectors

s=[0,5,6,60,66, 4,9,10,15,65,70,29,46]
sf=[4,9,10,15,65,70,29,46]
for i in sf:
    model.flip(i)
#for i in s:
    #print(f"Spin {i} has magnetization {model.vectors[i]}")
'''