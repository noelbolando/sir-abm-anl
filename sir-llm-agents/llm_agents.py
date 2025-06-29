"""llm_agents.py - this file contains the structure for LLM-driven agents in an SIR model."""

# Import libraries
import json
from ollama import Client

class LLMHealthAgent:
    def __init__(
            self, 
            unique_id, 
            role, 
            model="llama3",
            prompt_file = "llm_agent_prompts.json"
            ):
        
        self.unique_id = unique_id
        self.model = model
        self.client = Client()
        self.role = role
        self.day = 0
        self.role_description = self.load_role_from_json(prompt_file)

    def load_role_from_json(self, prompt_file):
        with open(prompt_file, "r") as f:
            prompts = json.load(f)
        if self.role not in prompts:
            raise ValueError(f"No role prompt assigned for role: {self.role}")
        return prompts[self.role]["role_description"]
    
    def interact(self, context):
        prompt = f"{self.role_description}\n\nDay {self.day} context:\n{context}\n\nWhat will you do today?"
        response = self.client.chat(model=self.model, messages=[
            {"role": "user",
             "content": prompt}
        ]) 
        return response["message"]["content"]
