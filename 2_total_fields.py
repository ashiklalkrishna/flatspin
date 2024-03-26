from flatspin import * 
import numpy as np 
import matplotlib.pyplot as plt
from flatspin.plotting import plot_vectors
import sys

plt.figure(dpi=200)

model = SquareSpinIceClosed()
'''for i in model.indices():
    plt.text(model.pos[i,0], model.pos[i,1], str(i), ha='center', va='center')
#plt.title('Model')'''
#model.spin[[0, 4, 39]] = -1 # flip spins 0, 4 and 39
#model.plot()

#dipolar field
h_dip = model.dipolar_fields()

plt.subplot(221)
#plt.title('h_dipolar_par')
plt.title('h_dipolar_perp')
quiv1 = model.plot(C=h_dip[:,1], cmap='coolwarm_r')
plt.colorbar(quiv1)

#external field
model.set_h_ext([.01,.005])
h_ext = model.external_fields()

plt.subplot(222)
#plt.title("h_ext")
plot_vectors(model.pos, model.h_ext, normalize=True)

plt.subplot(222)
#plt.title("h_ext_par")
plt.title("h_ext_perp")
quiv2 = model.plot(C=h_ext[:,1], cmap='coolwarm_r')
plt.colorbar(quiv2);

#thermal fields
model.set_temperature(600)
model.update_thermal_noise()
h_therm = model.thermal_fields()

plt.subplot(223)
#plt.title('h_thermal_par')
plt.title('h_thermal_perp')
quiv3 = model.plot(C=h_therm[:,1], cmap='coolwarm', normalize=True)
plt.colorbar(quiv3);

#total fields
h_tot = model.total_fields()

plt.subplot(224)
#plt.title("h_tot_par")
plt.title("h_tot_par")
quiv4 = model.plot(C=h_tot[:,1], cmap='coolwarm_r')
plt.colorbar(quiv4);

plt.tight_layout()
#plt.savefig(r'D:\Desktop\flatspin_code\2_fields\tot_fields_par(h_ext=[0.01,0.005]).png')
#plt.savefig(r'D:\Desktop\flatspin_code\2_fields\tot_fields_perp(h_ext=[0.01,0.005]).png')
#bbox_inches='tight')
plt.show()