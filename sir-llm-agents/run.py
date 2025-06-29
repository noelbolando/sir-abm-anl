"""run.py - run sample simulations with the llm agents"""

from llm_agents import LLMHealthAgent

agent = LLMHealthAgent(unique_id=0, role="infected")

context = "There are currently 100 infected people out of a population of 1000. Your symptoms are mild. You work in close proximity to other people. Do you go to work today?"
agent.day = 5
response = agent.interact(context)

print(f"[Agent {agent.unique_id}] Decision:\n{response}")
