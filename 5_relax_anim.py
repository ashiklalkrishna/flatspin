import flatspin
import matplotlib.pyplot as plt 
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
import numpy as np

model = flatspin.model.SquareSpinIceClosed()

# Strength of external field
H = np.linspace(0, 0.1, 100)
# Direction of the external field
phi = np.deg2rad(180 + 45)
h_dir = np.array([np.cos(phi), np.sin(phi)])

def do_reversal():
    yield model
    for h in H:
        model.set_h_ext(h * h_dir)
        if model.relax():
            # Only show plot when there were spin flips
            yield model

def do_plot(model):
    model.plot(ax=ax, replace=True)

fig, ax = plt.subplots( dpi=100)
anim = FuncAnimation(fig, do_plot, frames=do_reversal(), interval=500, blit=False, repeat=True, cache_frame_data=False)

# animation_file_path = "relax2.mp4"
# anim.save(animation_file_path, writer="ffmpeg", fps=1)

#plt.close() # Only show the animation
#HTML(anim.to_html5_video())
plt.show()