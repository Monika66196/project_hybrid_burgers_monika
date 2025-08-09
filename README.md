# Quantum–Classical Hybrid Solver for the 1D Viscous Burgers’ Equation

**Author:** Monika Sharma  
**GitHub Repository:** [project_hybrid_burgers_monika](https://github.com/Monika66196/project_hybrid_burgers_monika)

---

## 📌 Overview
Using Qiskit, this project makes a **"quantum-classical hybrid solver"** for the "1D viscous Burgers' equation."  
It shows how **variational quantum circuits** can get close to the viscous diffusion term and how a **classical solver** can deal with the nonlinear advection term.

The solver is designed with:
- **Low circuit depth** for NISQ devices  
- **Minimal qubit footprint** using amplitude encoding  
- **Noise robustness** with Aer simulation and error mitigation  
- **Scalability** to larger grids or even 2D/3D extensions

---

## 🧮 The Burgers’ Equation
We solve the **viscous Burgers' equation**:

\[
\frac{\partial u}{\partial t} + u \frac{\partial u}{\partial x} = \nu \frac{\partial^2 u}{\partial x^2}
\]

Where:
- \( u(x, t) \): fluid velocity
- \( \nu \): viscosity

This nonlinear PDE captures phenomena like **shock waves**, **steepening**, and **diffusion**.

---

## 📂 Project Structure


**Clone the Repository**

git clone https://github.com/Monika66196/project_hybrid_burgers_monika.git
cd project_hybrid_burgers_monika


**Install Dependencies**

pip install -r requirements.txt


##**Run the Jupyter Notebook**

jupyter notebook notebooks/hybrid_burgers_qiskit_monika_expanded_ibmq.ipynb

## If you want to run on a real IBM Quantum device:

Replace 'XXXXXXXXXXX' with your IBMQ API token in the notebook.

## Choose your backend using:

provider.backends()

## References

• Orús, R. (2019). Tensor networks for complex quantum systems. Nature Reviews Physics. https://doi.org/10.1038/s42254-019-0086-7

• Lubasch, M., et al. (2020). Variational quantum algorithms for nonlinear problems. Physical Review A. https://doi.org/10.1103/PhysRevA.101.010301

• Qiskit Contributors (2023). Qiskit Aer: A high-performance quantum simulator. https://qiskit.org/ecosystem/aer/

• Burgers, J. M. (1948). A mathematical model illustrating the theory of turbulence. Advances in Applied Mechanics. https://doi.org/10.1016/S0065-2156(08)70102-5

• McArdle, S., et al. (2020). Variational ansatz-based quantum simulation of imaginary time evolution. NPJ Quantum Information. https://doi.org/10.1038/s41534-019-0247-7

• Quantum Tensor Networks – https://arxiv.org/abs/quant-ph/9709024

• Hydrodynamic Schrödinger Equation – https://arxiv.org/abs/2204.00028

• Qiskit Documentation – https://qiskit.org/documentation/
