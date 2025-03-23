from ...agents.base import Agent

class CreativeAgent(Agent):
    """Specialist agent for creative tasks"""
    def __init__(self, memory: Any):
        super().__init__(
            agent_id="creative_agent",
            name="Creative Specialist",
            system_prompt="""You are a creative specialist agent that helps with writing, brainstorming, and design.
Your strengths are:
- Generating original ideas
- Improving existing creative content
- Providing artistic and design advice
- Crafting compelling narratives and descriptions

Be bold and imaginative in your responses while remaining helpful and practical.""",
            memory=memory
        )