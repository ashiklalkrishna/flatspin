import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from IPython.display import HTML
from flatspin.encoder import Triangle
from flatspin.plotting import plot_vectors, vector_colors
import numpy as np

def GSW(h_par, h_perp, b=1, c=1, beta=3, gamma=3):
    """ Generalized Stoner-Wohlfarth astroid  """
    sw = b*(1 - ((h_perp/c)**2)**(1/beta))**(gamma/2)
    sw[h_par<0] *= -1
    return sw

def plot_GSW(b=1, c=1, beta=3, gamma=3, ax=None, angle_range=(0, 2*np.pi), **kwargs):
    thetas = np.linspace(angle_range[0], angle_range[1], 3601)

    h_perp = c * np.cos(thetas)
    h_par = b * np.sin(thetas)
    
    kwargs.setdefault("label", rf"$b={b:g}, c={c:g}, \beta={beta:g}, \gamma={gamma:g}$")

    if ax is None:
        ax = plt.gca()
    return ax.plot(h_perp, GSW(h_par, h_perp, b, c, beta, gamma), **kwargs)

def animate_switching(model, H=0.15, phi=-100):
    # Reset system back to the polarized state
    model.polarize()
    hk = model.threshold.reshape((-1,1))

    # Set up figure and axes
    fig = plt.figure(facecolor='white')
    ax_astroid = plt.subplot2grid((2,3), (0,0), rowspan=2, colspan=2)
    ax_spin = plt.subplot2grid((2,3), (0,2))
    ax_h_ext = plt.subplot2grid((2,3), (1,2))

    # Set up external field (triangle wave)
    enc = Triangle(timesteps=64, H=H, phi=phi)
    h_ext = enc([1])

    # Plot astroid with field vector
    plt.sca(ax_astroid)
    line, = plot_GSW(*model.sw_params, angle_range=(np.pi, 2*np.pi))
    plot_GSW(*model.sw_params, angle_range=(0, np.pi), ls='dashed', color=line.get_color())
    origin = np.tile([0, 0], (model.spin_count, 1))
    plot_vectors(origin, origin, C=origin[:,0],
                 clim=(-.5,.5), cmap='bwr_r', scale=1, width=.05, pivot='tail', mask_zero=False)
    plt.xlabel('$h_\perp / h_k$')
    plt.ylabel('$h_\parallel / h_k$')

    # spin axis
    plt.sca(ax_spin)
    plt.axis('off')
    plt.title('spin')

    # h_ext axis
    plt.sca(ax_h_ext)
    plt.axis('off')
    plt.title('h_ext')

    def do_cycle():
        for h in h_ext:
            model.set_h_ext(h)
            model.relax()
            h_tot = model.total_fields()
            yield model.total_fields()

    def do_plot(h_tot):
        h_tot /= hk
        h_tot = np.column_stack([h_tot[:,1], h_tot[:,0]])
        plot_vectors(origin, h_tot, C=np.sign(h_tot[:,1]), ax=ax_astroid, replace=True)

        model.plot(ax=ax_spin, replace=True)

        h_ext = model.h_ext / hk
        plot_vectors(model.pos, h_ext, ax=ax_h_ext, replace=True, scale=.5, width=.1)

    anim = FuncAnimation(fig, do_plot, init_func=lambda: None, frames=do_cycle(), interval=200, blit=False, repeat=True, cache_frame_data=False)
    plt.close() # Only show the animation
    return anim

from flatspin.model import IsingSpinIce

model = IsingSpinIce(size=(1,1))
anim = animate_switching(model)
anim.save('animation.gif', writer='pillow')