"""stochastic_sir.py - Stochastic SIR model simulation"""

import numpy as np
import matplotlib.pyplot as plt

# Model parameters
np.random.seed(42)
population_size = 1000
# Boundary conditions
S0 = int(0.99 * population_size) # initial susceptible
I0 = int(0.01 * population_size) # initial infected
R0 = population_size - S0 - I0 # initial recovered

a = 0.03  # transmission probability per contact
b = 10   # contact rate (contacts per agent)
beta = a * b  # transmission rate
gamma = 0.1   # recovery rate
num_days = 100  # simulation run time
num_simulations = 10  # number of simulation runs

def run_stochastic_sir(S0, I0, R0, beta, gamma, num_days):
    """This function runs a single stochastic SIR simulation with initial boundary conditions."""
    # Initialize boundary conditions
    S = S0
    I = I0
    R = R0

    S_list = [S]
    I_list = [I]
    R_list = [R]

    # Run stochastic simulation for however many days the infection lasts
    for day in range(1, num_days):
        new_infections = np.random.binomial(S, 1 - (1 - beta / population_size) ** I)
        new_recoveries = np.random.binomial(I, gamma)

        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries

        S_list.append(S)
        I_list.append(I)
        R_list.append(R)

    return S_list, I_list, R_list

# Store all simulation results so we can run analysis
all_S = []
all_I = []
all_R = []

# Plotting the SIR curves
t = np.arange(num_days)
plt.figure(figsize=(12, 6))
for i in range(num_simulations):
    np.random.seed(i)
    S, I, R = run_stochastic_sir(S0, I0, R0, beta, gamma, num_days)
    all_S.append(S)
    all_I.append(I)
    all_R.append(R)

    plt.plot(t, S, color='green', alpha=0.3, label='Susceptible' if i == 0 else "")
    plt.plot(t, I, color='red', alpha=0.3, label='Infected' if i == 0 else "")
    plt.plot(t, R, color='gray', alpha=0.3, label='Recovered' if i == 0 else "")

# Convert to arrays for averaging run results
mean_S = np.mean(np.array(all_S), axis=0)
mean_I = np.mean(np.array(all_I), axis=0)
mean_R = np.mean(np.array(all_R), axis=0)

# Plot average SIR curves
plt.plot(t, mean_S, color='green', linewidth=2.5, label='Avg Susceptible')
plt.plot(t, mean_I, color='red', linewidth=2.5, label='Avg Infected')
plt.plot(t, mean_R, color='gray', linewidth=2.5, label='Avg Recovered')
plt.xlabel('Time (days)')
plt.ylabel('Number of Individuals')
plt.title(f'{num_simulations} Stochastic SIR Simulations + Averages')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
