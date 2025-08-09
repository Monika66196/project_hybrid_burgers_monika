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
