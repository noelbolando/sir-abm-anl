"""app.py - file for SIR ABM"""

from model import State, VirusOnNetwork
from mesa.visualization import Slider, SolaraViz, make_plot_component, make_space_component
import solara

def agent_portrayal(agent):
    """
    Helper function for agent portrayal
        Infected: red
        Susceptible: green
        Recovered: gray
    """
    node_color_dict = {
        State.INFECTED: "tab:red",
        State.SUSCEPTIBLE: "tab:green",
        State.RECOVERED: "tab:gray"
    }
    return {"color": node_color_dict[agent.state], "size": 100}

model_params = {
    "seed": {
        "type": "InputText",
        "value": 42,
        "label": "Random Seed",
    },
    "population": Slider(
        label="Population Size",
        value=100,
        min=10,
        max=1000000,
        step=1,
    ),
    "num_nearest_neighbors": Slider(
        label="Number Nearest Neighbors",
        value=10,
        min=5,
        max=10,
        step=1,
    ),
    "initial_number_infected": Slider(
        label="Number Infected",
        value=1,
        min=1,
        max=10,
        step=1,
    ),
    "beta": Slider(
        label="Beta",
        value=0.4,
        min=0.0,
        max=1.0,
        step=0.1,
    ),
    "gamma": Slider(
        label="Gamma",
        value=0.1,
        min=0.0,
        max=1.0,
        step=0.1,
    )
}

def post_process_lineplot(ax):
    """Helper function for portraying SIR graph"""
    ax.set_ylim(ymin=0)
    ax.set_ylabel("Number of Agents")
    ax.legend(bbox_to_anchor=(1.05, 1.0), loc="upper left")


SpacePlot = make_space_component(agent_portrayal)
StatePlot = make_plot_component(
    {"Infected": "tab:red", "Susceptible": "tab:green", "Recovered": "tab:gray"},
    post_process=post_process_lineplot
)

# Initializing an instance of the web page
@solara.component
def Page():
    solara.Title("SIR Model with LLM Control Agent")

    model_reactive = solara.use_reactive(VirusOnNetwork())

    with solara.ColumnsResponsive(12, large=[8,4]):
        with solara.Column(style={"padding": "1em"}):
            solara.Markdown("## 🧫 SIR Virus Simulation")

            SolaraViz(
                model_reactive.value,
                components=[
                    SpacePlot,
                    StatePlot
                ],
                model_params=model_params,
                name="SIR Virus Model"
            )
