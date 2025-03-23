#!/usr/bin/env python3
"""
run.py - Main entry point for the Swarm Agents system
"""

import os
import sys
import logging
from typing import Optional
import typer

# Add the project directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import our swarm agent implementation
from swarm_agents import SwarmAgentSystem

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("logs/swarm_agents.log"),
        logging.StreamHandler()
    ]
)

# Create a Rich console for pretty output if available
try:
    from rich.console import Console
    from rich.panel import Panel
    from rich.text import Text
    console = Console()
except ImportError:
    # Fallback to standard print if Rich is not installed
    class FallbackConsole:
        def print(self, *args, **kwargs):
            print(*args)
        def input(self, prompt):
            return input(prompt)
    console = FallbackConsole()

app = typer.Typer()

@app.command()
def main(
    debug: bool = False,
    api_key: Optional[str] = None,
):
    """
    Run the Swarm Agents system in interactive mode.
    """
    # Create logs directory if it doesn't exist
    os.makedirs("logs", exist_ok=True)
    
    # Show welcome message
    console.print("Swarm Agents System")
    console.print("A collaborative multi-agent AI system")
    
    # Set debug mode if specified
    if debug:
        logging.getLogger().setLevel(logging.DEBUG)
        console.print("Debug mode enabled")
    
    # Set API key if provided
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    
    # Initialize the swarm agent system
    try:
        swarm = SwarmAgentSystem()
        console.print("✓ Swarm Agent System initialized successfully")
    except Exception as e:
        console.print(f"✗ Failed to initialize Swarm Agent System: {e}")
        return
    
    # Main interaction loop
    console.print("\nEnter your queries below. Type 'exit' or 'quit' to end.")
    
    while True:
        # Get user input
        user_input = console.input("\nYou: ")
        
        # Check for exit command
        if user_input.lower() in ("exit", "quit", "q"):
            break
        
        try:
            # Process the user message
            result = swarm.process_message(user_input)
            
            # Display the response with appropriate styling
            agent_name = result["agent"]
            response = result["response"]
            
            console.print(f"\n{agent_name}:")
            console.print(response)
            
        except Exception as e:
            console.print(f"Error processing message: {e}")
    
    console.print("\nThank you for using Swarm Agents!")


if __name__ == "__main__":
    app()