"""
quantum_utils.py
Quantum encoding and diffusion approximation functions using Qiskit.
"""

import numpy as np
from qiskit import QuantumCircuit, Aer, transpile
from qiskit.circuit.library import TwoLocal
from qiskit_aer import AerSimulator

def amplitude_encode(data):
    """
    Normalize and amplitude-encode data into a quantum state.
    Parameters:
        data : list or np.array
    Returns:
        normalized numpy array suitable for Initialize gate
    """
    norm = np.linalg.norm(data)
    if norm == 0:
        raise ValueError("Cannot encode zero vector.")
    return data / norm

def build_monika_ansatz(num_qubits, reps=2):
    """
    Build Monika's custom TwoLocal ansatz.
    """
    return TwoLocal(
        num_qubits,
        rotation_blocks=['ry', 'rz'],
        entanglement_blocks='cz',
        entanglement='linear',
        reps=reps
    )

def run_quantum_circuit(circuit, shots=1024):
    """
    Run a given quantum circuit on Qiskit's Aer simulator.
    """
    sim = AerSimulator()
    t_qc = transpile(circuit, sim)
    result = sim.run(t_qc, shots=shots).result()
    return result.get_counts()

def quantum_diffusion_step(u, ansatz, params):
    """
    Apply quantum-based diffusion approximation (placeholder).
    Parameters:
        u       : velocity field (numpy array)
        ansatz  : Qiskit ansatz circuit
        params  : parameters for ansatz
    Returns:
        u_new   : updated velocity field
    """
    # Placeholder: classical smoothing to mimic quantum op
    kernel = np.array([0.25, 0.5, 0.25])
    u_smooth = np.convolve(u, kernel, mode='same')
    return u_smooth
