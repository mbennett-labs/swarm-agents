import os
from typing import List, Dict, Any, Optional
import json
import openai

class Message:
    """Simple class to represent messages between agents"""
    def __init__(self, role: str, content: str):
        self.role = role
        self.content = content
    
    def to_dict(self) -> Dict[str, str]:
        return {"role": self.role, "content": self.content}


class Agent:
    """Base agent class"""
    def __init__(self, agent_id: str, name: str, system_prompt: str, memory: Any):
        self.agent_id = agent_id
        self.name = name
        self.system_prompt = system_prompt
        self.memory = memory
    
    def think(self, input_message: str) -> str:
        """Process the input and generate a response"""
        messages = [
            {"role": "system", "content": self.system_prompt},
            *self.memory.get_recent_history(5),
            {"role": "user", "content": input_message}
        ]
        
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0.7,
                max_tokens=500
            )
            return response.choices[0].message["content"]
        except Exception as e:
            print(f"Error in agent {self.name}: {e}")
            return f"I'm sorry, I encountered an error: {e}"
    
    def respond(self, input_message: str) -> str:
        """Generate a response and update memory"""
        response = self.think(input_message)
        
        # Update memory
        self.memory.add_to_history(Message("user", input_message))
        self.memory.add_to_history(Message("assistant", response))
        
        return response