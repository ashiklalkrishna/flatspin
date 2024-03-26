````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````````"""
Generalized Stoner-Wohlfarth Astroid
"""
import numpy as np

def rotate_points(x, y, theta):
    return (x * np.cos(theta) - y * np.sin(theta),
            x * np.sin(theta) + y * np.cos(theta))

def gsw(h_par, b=1.0, c=1.0, beta=3.0, gamma=3.0, hc=1.0):
    """ Generalized Stoner-Wohlfarth Astroid (explicit form) """
    h_par = h_par / (b * hc)
    h_perp = c * hc * (1 - (h_par**2)**(1/gamma))**(beta/2)
    return h_perp

def gsw_implicit(h_par, h_perp, b=1.0, c=1.0, beta=3.0, gamma=3.0, hc=1.0):
    """ Generalized Stoner-Wohlfarth Astroid (implicit form) """
    h_par = h_par / (b * hc)
    h_perp = h_perp / (c * hc)
    return (h_par**2)**(1/gamma) + (h_perp**2)**(1/beta) - 1

def gsw_astroid(b=1.0, c=1.0, beta=3.0, gamma=3.0, hc=1.0,
                rotation=0, resolution=361, angle_range=(0, 2*np.pi)):
    """ Generate samples from the Generalized Stoner-Wohlfarth Astroid """

    thetas = np.linspace(angle_range[0], angle_range[1], resolution)

    h_par = b * hc * np.cos(thetas)
    h_perp = gsw(h_par, b, c, beta, gamma, hc)
    h_perp[(thetas % (2*np.pi)) > np.pi] *= -1

    h_par, h_perp = rotate_points(h_par, h_perp, np.deg2rad(rotation))

    return np.column_stack([h_par, h_perp])
