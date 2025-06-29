"""agent.py - file for SIR ABM"""

from enum import Enum
from mesa import Agent


class State(Enum):
    SUSCEPTIBLE = 0
    INFECTED = 1
    RECOVERED = 2


class VirusAgent(Agent):
    """Individual Agent definition and its properties/interaction methods."""

    def __init__(
        self,
        model,
        initial_state,
        beta,
        virus_check_frequency,
        gamma
    ):
        super().__init__(model)

        self.state = initial_state
        self.beta = beta
        self.virus_check_frequency = virus_check_frequency
        self.gamma = gamma

    def try_to_infect_neighbors(self):
        """Define how SUSCEPTIBLE agents become INFECTED"""
        neighbors_nodes = self.model.grid.get_neighborhood(
            self.pos, include_center=False
        )
        susceptible_neighbors = [
            agent
            for agent in self.model.grid.get_cell_list_contents(neighbors_nodes)
            if agent.state is State.SUSCEPTIBLE
        ]
        for a in susceptible_neighbors:
            if self.random.random() < self.beta:
                a.state = State.INFECTED

    def try_recover(self):
        # Try to remove
        if self.random.random() < self.gamma:
            # Success
            self.state = State.RECOVERED
        else:
            # Failed
            self.state = State.INFECTED

    def check_situation(self):
        if (self.state is State.INFECTED) and (
            self.random.random() < self.virus_check_frequency
        ):
            self.try_recover()

    def step(self):
        if self.state is State.INFECTED:
            self.try_to_infect_neighbors()
        self.check_situation()
            
