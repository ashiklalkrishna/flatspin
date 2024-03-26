import flatspin.encoder as en
import matplotlib.pyplot as plt
import numpy as np

def expand_dims(input):
    """ Ensure last dimension of input is single-dimensional """
    if input.shape[-1] != 1:
        return np.expand_dims(input, -1)
    return input
def check_input(input):
    input = np.array(input)
    if len(input.shape) == 1:
        return np.expand_dims(input, -1)
    return input

def broadcast_waveform(input, waveform):
    """ Broadcast waveform over input """
    input = check_input(input)
    # multiply input by waveform (broadcasting rules apply)
    out = input * waveform
    # roll last axis to the first (time)
    out = np.moveaxis(out, -1, 1)
    # finally concatenate it
    out = np.concatenate(out)
    return out

def scale(input, H0=0, H=1):
    """ Scale input to range [H0, H] """
    return H0 + input * (H - H0)

def sin(input, timesteps=100, phase=0):
    """ Multiply input by sine wave """
    ph = np.deg2rad(phase)
    t = np.linspace(ph, 2 * np.pi + ph, timesteps, endpoint=False)
    waveform = np.sin(t)
    #return broadcast_waveform(input, waveform)
    return waveform

def fixed_vector(input, phi=30):
    """ Convert scalar input to vectors at some angle phi """
    input = check_input(input)
    theta = np.deg2rad(phi)
    # add one dimension to broadcast vector
    input = expand_dims(input)
    vector = [np.cos(theta), np.sin(theta)]
    out = input * vector
    return out

def rotate(input, timesteps=100, phase=0):
    """ Multiply input by rotation vector """
    ph = np.deg2rad(phase)
    t = np.linspace(ph, 2 * np.pi + ph, timesteps, endpoint=False)
    cos = broadcast_waveform(input, np.cos(t))
    sin = broadcast_waveform(input, np.sin(t))
    return np.stack([cos, sin], axis=-1)

class Rotate(en.Encoder):
    """Encode input as the amplitude of a rotating global field.

    The amplitude is scaled between `H0` and `H`.
    The rotating field has a resolution `timesteps` samples.
    The rotating field has a phase of `phase` degrees.
    """

    steps = (scale, rotate)

class Sine(en.Encoder):
    """Encode input as the amplitude of a sinusoidal global field.

    The amplitude is scaled between `H0` and `H`.
    The field has a fixed angle of `phi` degrees.
    The sine wave has a resolution `timesteps` samples.
    The sine wave has a phase of `phase` degrees.
    """

    steps = (scale, sin, fixed_vector)

encoder = en.Rotate()
encoder.set_params(H0=1, H=1, timesteps=100, phase=0)
input = np.linspace(1, 0, 1, endpoint=False)
h_ext = encoder(input)

print(rotate(input, timesteps=6, phase=0))

plt.title(str(encoder))
plt.plot(h_ext[:,0],  label="h_ext[0]")
plt.plot(h_ext[:,1], label="h_ext[1]")
plt.xlabel("t")
plt.legend();
plt.show()