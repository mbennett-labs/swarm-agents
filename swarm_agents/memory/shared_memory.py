from typing import List, Dict, Any

class Memory:
    """Shared memory for agents to store and retrieve information"""
    def __init__(self):
        self.facts = []
        self.conversation_history = []
    
    def add_fact(self, fact: str):
        self.facts.append(fact)
    
    def get_facts(self) -> List[str]:
        return self.facts
    
    def add_to_history(self, message: Any):
        self.conversation_history.append(message.to_dict())
    
    def get_recent_history(self, n: int = 10) -> List[Dict[str, str]]:
        return self.conversation_history[-n:]