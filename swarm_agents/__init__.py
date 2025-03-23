from .agents.base import Agent, Message
from .agents.triage import TriageAgent
from .agents.specialists.research import ResearchAgent
from .agents.specialists.creative import CreativeAgent
from .agents.specialists.code import CodeAgent
from .agents.specialists.math import MathAgent
from .memory.shared_memory import Memory

class SwarmAgentSystem:
    """Main class that coordinates the swarm of agents"""
    def __init__(self):
        self.memory = Memory()
        
        # Initialize specialist agents
        self.research_agent = ResearchAgent(self.memory)
        self.creative_agent = CreativeAgent(self.memory)
        self.code_agent = CodeAgent(self.memory)
        self.math_agent = MathAgent(self.memory)
        
        # Initialize triage agent with specialists
        self.triage_agent = TriageAgent(self.memory)
        self.triage_agent.add_specialist(self.research_agent)
        self.triage_agent.add_specialist(self.creative_agent)
        self.triage_agent.add_specialist(self.code_agent)
        self.triage_agent.add_specialist(self.math_agent)
    
    def process_message(self, user_message: str) -> dict:
        """Process a user message through the swarm agent system"""
        result = self.triage_agent.route_message(user_message)
        return result

__all__ = ['SwarmAgentSystem', 'Agent', 'Message', 'Memory', 
          'TriageAgent', 'ResearchAgent', 'CreativeAgent', 'CodeAgent', 'MathAgent']