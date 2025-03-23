from typing import Dict, Any
from ..agents.base import Agent

class TriageAgent(Agent):
    """Coordinator agent that routes tasks to appropriate specialist agents"""
    def __init__(self, memory: Any, specialists: Dict[str, Agent] = None):
        super().__init__(
            agent_id="triage",
            name="Triage Agent",
            system_prompt="""You are a triage agent that determines which specialist should handle a given request.
Available specialists:
- research_agent: For questions requiring in-depth research and analysis
- creative_agent: For creative tasks like writing, brainstorming, or design ideas
- code_agent: For programming-related questions and tasks
- math_agent: For mathematical calculations and problems

Respond ONLY with the name of the specialist who should handle this request. If you're unsure, respond with "research_agent".""",
            memory=memory
        )
        self.specialists = specialists or {}
    
    def add_specialist(self, agent: Agent):
        """Add a specialist agent to the triage system"""
        self.specialists[agent.agent_id] = agent
    
    def route_message(self, user_message: str) -> Dict[str, Any]:
        """Route the message to the appropriate specialist and return their response"""
        specialist_id = self.think(user_message).strip().lower()
        
        # Handle case where the specialist doesn't exist
        if specialist_id not in self.specialists:
            specialist_id = "research_agent"
            if specialist_id not in self.specialists:
                return {
                    "agent": "triage",
                    "response": f"No specialist found for {specialist_id}. Please add specialists to the system."
                }
        
        # Route to the specialist
        specialist = self.specialists[specialist_id]
        response = specialist.respond(user_message)
        
        return {
            "agent": specialist.name,
            "agent_id": specialist.agent_id,
            "response": response
        }