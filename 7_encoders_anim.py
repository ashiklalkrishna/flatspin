import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
from matplotlib import ticker
from IPython.display import HTML
from flatspin.plotting import plot_vectors
import textwrap

def animate_h_ext(h_ext, title="", interval=100, cmap='rainbow'):
    fig, ax = plt.subplots()
    
    # Axes setup
    ax.set_title(textwrap.fill(title))
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.yaxis.set_major_locator(ticker.MultipleLocator(1))
    ax.tick_params(bottom=False, left=False, labelbottom=False, labelleft=False)

    # Normalize vectors to unit length
    nmax = np.max([np.linalg.norm(h_ext.reshape((-1,2)), axis=-1)])
    if nmax != 0:
        h_ext /= nmax

    # Positions of vectors
    if len(h_ext.shape) == 4:
        # Spatial field
        xx, yy = np.meshgrid(np.arange(h_ext.shape[1]), np.arange(h_ext.shape[2]))
        XY = np.column_stack([xx.ravel(), yy.ravel()])
    else:
        # Global field (single arrow)
        XY = [[0,0]]

    # Colors
    C = np.linspace(0, 1, len(XY), endpoint=False)
    
    def do_animate(i):
        plot_vectors(XY, h_ext[i], C, clim=(0, 1), cmap=cmap, ax=ax, replace=True, mask_zero=False)

    anim = FuncAnimation(fig, do_animate, frames=len(h_ext), interval=interval, blit=False)
    #plt.close() # Only show the animation
    return HTML(anim.to_jshtml(fps=1000/interval))
    

from flatspin.encoder import Rotate

# Gradually decreasing rotating field
encoder = Rotate(H=0.1, timesteps=16)
input = np.linspace(1, 0, 10, endpoint=False)
h_ext = encoder(input)

animate_h_ext(h_ext, str(encoder))
#plt.show()