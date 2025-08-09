"""
classical_solver.py
Classical solver functions for the Burgers' equation advection step.
"""

import numpy as np

def burgers_rhs(u, dx, nu):
    """
    Compute the right-hand side of the viscous Burgers' equation (semi-discrete form).
    Parameters:
        u  : velocity array
        dx : spatial step
        nu : viscosity coefficient
    Returns:
        du/dt array
    """
    dudx = (np.roll(u, -1) - np.roll(u, 1)) / (2.0 * dx)
    d2udx2 = (np.roll(u, -1) - 2 * u + np.roll(u, 1)) / (dx ** 2)
    return -u * dudx + nu * d2udx2

def step_rk3(u, dt, dx, nu):
    """
    Advance one timestep using the SSP-RK3 scheme.
    """
    u1 = u + dt * burgers_rhs(u, dx, nu)
    u2 = 0.75 * u + 0.25 * (u1 + dt * burgers_rhs(u1, dx, nu))
    u3 = (1.0/3.0) * u + (2.0/3.0) * (u2 + dt * burgers_rhs(u2, dx, nu))
    return u3
