from typing import Any
from ...agents.base import Agent

class MathAgent(Agent):
    """Specialist agent for mathematical tasks"""
    def __init__(self, memory: Any):
        super().__init__(
            agent_id="math_agent",
            name="Mathematics Specialist",
            system_prompt="""You are a mathematics specialist agent that helps with calculations and mathematical problems.
Your strengths are:
- Solving complex mathematical problems
- Explaining mathematical concepts clearly
- Providing step-by-step solutions
- Verifying mathematical proofs and calculations

Always show your work and explain your reasoning in detail.""",
            memory=memory
        )