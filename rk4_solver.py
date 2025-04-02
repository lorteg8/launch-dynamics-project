import numpy as np

def rk4_step(f, t, y, dt, params):
    k1 = f(t, y, params)
    k2 = f(t + dt/2, y + dt/2 * k1, params)
    k3 = f(t + dt/2, y + dt/2 * k2, params)
    k4 = f(t + dt, y + dt * k3, params)
    return y + dt/6 * (k1 + 2*k2 + 2*k3 + k4)

def launch_dynamics(t, state, params):
    x, v = state
    m = params["m0"] - params["alpha"] * t
    if m <= 0:
        return np.array([0.0, 0.0])
    rho = params["rho0"] * np.exp(-x / params["H"])
    D = 0.5 * rho * params["Cd"] * params["A"] * v**2 * np.sign(v)
    a = (params["T"] - D - m * 9.81) / m
    return np.array([v, a])

def simulate(params, t_max=120, dt=0.1):
    t_vals = [0]
    y_vals = [np.array([0.0, 0.0])]
    t = 0
    while t < t_max:
        y_next = rk4_step(launch_dynamics, t, y_vals[-1], dt, params)
        t += dt
        if params["m0"] - params["alpha"] * t <= 0:
            break
        y_vals.append(y_next)
        t_vals.append(t)
    return np.array(t_vals), np.array(y_vals)
