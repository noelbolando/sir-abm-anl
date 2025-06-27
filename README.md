# Basic SIR Model #

## Agent States ##
This SIR model seperates a population into three states:
    Susceptible agents (S)
    Infected agents (I)
    Recovered agents (R)

## Model Parameters ##
Where the following parameters simulate how these states change over time:
    beta: transmission rate
    gamma: recovery rate

## Agent States as ODEs ##
The following ODEs are used to express agent states and how they change over time, considering parameters beta and gamma:
    dSdt = -beta * S * I
    dIdt = beta * S * (I - gamma) * I
    dRdt = gamma * I

## Model Output -- SIR Curve ##
The following graph is output after running the model based on the parameters hard-coded into the script. Varying the parameters will alter the output of this graph.
![alt text](<Screenshot 2025-06-27 at 2.43.32 PM.png>)