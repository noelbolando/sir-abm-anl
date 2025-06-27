"""model.py - this file contains scripts for SIR model"""

# Import libraries
import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Define the SIR model equations
def sir_model(y, t, beta, gamma):
    """
    Helper function to define SIR variables and functions.
        S: susceptible agents
        I: infected agents
        R: recovered agents
        beta: transmission rate
        gamma: recovery rate
        ODEs track rate of susceptibility, infection, and recovery over time:
            dSdt: rate of change of susceptible agents with respect to time
            dIdt: rate of change of infected agents with resepct to time
            dRdt: rate of change of recovered agents with respect to time
    """
    S, I, R = y
    dSdt = -beta * S * I
    dIdt = beta * S * I - gamma * I
    dRdt = gamma * I
    return [dSdt, dIdt, dRdt]

# Model parameters
S0 = 0.99 # 99% of the population is susceptible at t=0
I0 = 0.01 # 1% of the population is infected at t=0
R0 = 0.00 # 0% of the population is recovered at t=0
y0 = [S0, I0, R0]
beta = 0.3 # transmission rate
gamma = 0.1 # recovery rate
num_days = 200 # simulation run time
t = np.linspace(0, num_days, num_days) # time vector

# Solution for SIR model equations
solution = odeint(sir_model, y0, t, args=(beta, gamma))

# Extract the model results
S, I, R = solution.T

# Plot the model results
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Susceptible')
plt.plot(t, I, label='Infected')
plt.plot(t, R, label='Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Proportion of Population (%)')
plt.title(f'SIR Model Simulation for {num_days} Days')
plt.legend()
plt.grid(True)
plt.show()


