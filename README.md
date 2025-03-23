# Swarm Agents

![Swarm Agents Banner](https://via.placeholder.com/1200x300/4CAF50/FFFFFF?text=Swarm+Agents)

## Overview

Swarm Agents is a modular, extensible framework for creating collaborative AI agent systems. Inspired by swarm intelligence in nature, this project enables multiple specialized AI agents to work together to solve complex problems more effectively than a single agent could alone.

Through a coordinated system of triage and specialist agents, swarm intelligence emerges as agents collaborate, share knowledge, and tackle different aspects of a problem based on their unique capabilities.

## Key Features

- **Triage System**: Intelligent routing of queries to the most appropriate specialist agent
- **Specialist Agents**: Purpose-built agents with different strengths and capabilities
- **Shared Memory**: A collective knowledge base that allows agents to build on each other's work
- **Extensible Framework**: Easily add new specialist agents with different abilities
- **Conversation History**: Agents maintain context throughout interactions

## Agent Types

| Agent | Description |
|-------|-------------|
| **Triage Agent** | Routes incoming queries to the appropriate specialist based on content analysis |
| **Research Agent** | Specializes in gathering, synthesizing and presenting information |
| **Creative Agent** | Focuses on creative tasks like writing, brainstorming, and design |
| **Code Agent** | Handles programming tasks and technical implementations |
| **Math Agent** | Specializes in mathematical calculations and problem-solving |

## Architecture
┌─────────────────┐
│                 │
│   User Input    │
│                 │
└────────┬────────┘
│
▼
┌─────────────────┐     ┌─────────────────┐
│                 │     │                 │
│  Triage Agent   │◄───►│  Shared Memory  │
│                 │     │                 │
└────────┬────────┘     └─────────────────┘
│                      ▲
▼                      │
┌─────────────────┐             │
│   Specialist    │             │
│     Agents      ├─────────────┘
└─────────────────┘

## Use Cases

- **Research Assistant**: Synthesize information from multiple sources
- **Creative Projects**: Generate and refine ideas for content creation
- **Software Development**: Debug code, explain concepts, and suggest improvements
- **Education**: Explain complex topics with the appropriate specialist
- **Problem-Solving**: Break down and solve multi-faceted problems

## Getting Started

### Prerequisites

- Python 3.8+
- OpenAI API key (or other compatible LLM API)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mbennett-labs/swarm-agents.git
   cd swarm-agents