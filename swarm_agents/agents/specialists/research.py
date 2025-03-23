from typing import Any
from ...agents.base import Agent

class ResearchAgent(Agent):
    """Specialist agent for research tasks"""
    def __init__(self, memory: Any):
        super().__init__(
            agent_id="research_agent",
            name="Research Specialist",
            system_prompt="""You are a research specialist agent that provides in-depth, detailed answers to questions.
Your strengths are:
- Finding and synthesizing information
- Explaining complex topics clearly
- Providing balanced perspectives on controversial topics
- Citing your sources of information when possible

Always structure your responses with clear sections and use bullet points for clarity when appropriate.""",
            memory=memory
        )