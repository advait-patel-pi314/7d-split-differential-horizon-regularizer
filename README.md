
# 7D Split-Differential Horizon Regularizer (The Grand Synthesis)

This repository houses the numerical implementation of the 7-dimensional phase-space coordinate vector tracking system across the Schwarzschild event horizon boundary. It validates the split exterior differentiation routine and the boundary-damped interpolation operator that regularizes the classical radial metric singularity.

## 📐 Calculus Architecture

To prevent higher-order cross-derivatives from triggering early algebraic truncations, the manifold partitions its tangent space via a direct sum ($T\mathcal{M}^7 = T_{\text{GR}}^4 \oplus T_{\text{QC}}^3$), executing independent exterior differentiation:

$$\mathbf{d} = \mathbf{d}_{\text{GR}} + \mathbf{d}_{\text{QC}}$$

When evaluated at the event horizon radius ($r = 2M$), a specialized localized boundary-damped operator maps the coordinate strain cleanly out of the real spacetime line and shifts it into the nilpotent configuration fiber, stabilizing the metric index as a finite ring invariant:

$$g_{rr}^{\text{regularized}}\Big|_{r=2M} = \frac{1}{j}$$

## 🛠️ Key Features

* **7D Phase-Space Tracker:** Coordinate tracking modules handling the joint base vector $\mathbf{X} = (x, y, z, t, \tau, \phi, \chi)$.
* **Split Derivative Simulation:** Independent processing arrays for macroscopic relativity and microscopic quantum configurations before metric tensor recombination.
* **Horizon Transition Profiler:** Numerical modeling demonstrating the smooth convergence of $g_{rr}$ from flat Minkowski space at long range ($r \to \infty$) down to the stable $1/j$ boundary value.

## 📦 Getting Started

### Prerequisites
* Python 3.8+
* NumPy / Matplotlib

### Execution
Run the event horizon transition simulation:
```bash
python run_horizon_regularization.py
