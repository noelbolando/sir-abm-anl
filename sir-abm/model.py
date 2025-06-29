"""model.py - file for SIR ABM"""

import math

import networkx as nx

import mesa
from mesa import Model
from agent import State, VirusAgent


def number_state(model, state):
    return sum(1 for a in model.grid.get_all_cell_contents() if a.state is state)


def number_infected(model):
    return number_state(model, State.INFECTED)


def number_susceptible(model):
    return number_state(model, State.SUSCEPTIBLE)


def number_recovered(model):
    return number_state(model, State.RECOVERED)


class VirusOnNetwork(Model):
    """A virus model with some number of agents."""

    def __init__(
        self,
        population=10,
        num_nearest_neighbors=10,
        initial_number_infected=1,
        beta=0.4,
        virus_check_frequency=0.4,
        gamma=0.1,
        seed=None,
    ):
        super().__init__(seed=seed)
        self.population = population
        prob = num_nearest_neighbors / population
        self.G = nx.erdos_renyi_graph(n=population, p=prob)
        self.grid = mesa.space.NetworkGrid(self.G)

        self.initial_outbreak_size = (initial_number_infected if initial_number_infected <= population else population)
        self.beta = beta
        self.virus_check_frequency = virus_check_frequency
        self.gamma = gamma

        self.datacollector = mesa.DataCollector(
            {
                "Infected": number_infected,
                "Susceptible": number_susceptible,
                "Recovered": number_recovered
            }
        )
        # Create SUSCEPTIBLE agents.
        for node in self.G.nodes():
            a = VirusAgent(
                self,
                State.SUSCEPTIBLE,
                beta,
                virus_check_frequency,
                gamma
            )
        
            # Add the SUSCEPTIBLE agents to the model.
            self.grid.place_agent(a, node)

        # Infect some nodes
        infected_nodes = self.random.sample(list(self.G), self.initial_outbreak_size)
        # Randomly infect some of the agents based on the initial_outbreak_size variable.
        for a in self.grid.get_cell_list_contents(infected_nodes):
            a.state = State.INFECTED

        self.running = True
        self.datacollector.collect(self)

    def step(self):
        self.agents.shuffle_do("step")
        # collect data
        self.datacollector.collect(self)
