# AE370 Project 1 – Reusable Spaceplane Ascent Modeling

This project models the vertical ascent of a reusable spaceplane using a nonlinear dynamical system with time-varying mass and atmospheric drag. We implement a fourth-order Runge–Kutta method (RK4) to simulate system behavior and explore design questions through parameter sweeps.

## 📁 Repository Structure

- `rk4_solver.py`: Contains the RK4 integrator and ODE definitions.
- `simulations/`: Scripts to run convergence tests and generate all figures for the report.
- `report/`: LaTeX source for the final AIAA-formatted technical report.
- `fig_outputs/`: All figures used in the final report are saved here.
- `requirements.txt`: Lists Python dependencies.

## 🧪 How to Run

Clone the repository and install dependencies:

```bash
git clone https://github.com/YOUR_USERNAME/launch-dynamics-project.git
cd launch-dynamics-project
pip install -r requirements.txt
```

Then generate all results:

```bash
python simulations/convergence_study.py
python simulations/param_sweeps.py
```

Plots will be saved in `simulations/fig_outputs/`.

## 📄 Report

You can compile the report from the `report/` folder using Overleaf or a local LaTeX compiler.

## 📜 License

This project is released under the MIT License.
