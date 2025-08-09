"""
grid_utils.py
Grid creation and initial conditions for Burgers' solver.
"""
import numpy as np

def make_grid(L=1.0, N=16):
    x = np.linspace(0, L, N, endpoint=False)
    dx = x[1] - x[0]
    return x, dx

def initial_sine(x):
    return np.sin(2*np.pi*x)

def initial_riemann(x, left=1.0, right=0.0, x0=0.5):
    u = np.where(x < x0, left, right).astype(float)
    kernel = np.array([0.25, 0.5, 0.25])
    for _ in range(2):
        u = np.convolve(u, kernel, mode='same')
    return u
