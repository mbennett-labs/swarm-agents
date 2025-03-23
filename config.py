# config.py - Configuration for the Swarm Agent system

# Agent configuration
AGENT_CONFIG = {
    # Triage agent settings
    "triage": {
        "name": "Triage Agent",
        "model": "gpt-3.5-turbo",
        "temperature": 0.2,  # Lower temperature for more deterministic routing
        "max_tokens": 50,    # Triage responses should be short
    },
    
    # Specialist agent settings
    "research_agent": {
        "name": "Research Specialist",
        "model": "gpt-4",    # Use more powerful model for research
        "temperature": 0.7,
        "max_tokens": 1000,  # Longer responses for detailed research
    },
    
    "creative_agent": {
        "name": "Creative Specialist",
        "model": "gpt-4",
        "temperature": 0.9,  # Higher temperature for more creative responses
        "max_tokens": 800,
    },
    
    "code_agent": {
        "name": "Code Specialist",
        "model": "gpt-4",
        "temperature": 0.3,  # Lower temperature for more precise code generation
        "max_tokens": 1200,  # Allow for longer code snippets
    },
    
    "math_agent": {
        "name": "Mathematics Specialist",
        "model": "gpt-4",
        "temperature": 0.1,  # Lower temperature for accurate calculations
        "max_tokens": 600,
    }
}

# Memory settings
MEMORY_CONFIG = {
    "max_history_items": 20,      # Number of conversation turns to retain
    "facts_database": "sqlite",   # Storage type for persistent facts
    "facts_db_path": "data/facts.db"
}

# System settings
SYSTEM_CONFIG = {
    "debug_mode": False,
    "log_level": "INFO",
    "log_file": "logs/swarm_agents.log",
    "api_timeout": 30,  # Seconds
}

# Define agent specializations for routing
AGENT_SPECIALIZATIONS = {
    "research_agent": [
        "information", "facts", "history", "science", "explain", "describe",
        "compare", "analyze", "research", "summary", "overview", "details"
    ],
    
    "creative_agent": [
        "write", "create", "design", "story", "poem", "script", "creative",
        "imagine", "brainstorm", "idea", "content", "marketing", "slogan"
    ],
    
    "code_agent": [
        "code", "program", "function", "script", "algorithm", "debug",
        "programming", "python", "javascript", "java", "html", "css",
        "api", "database", "sql", "git", "docker", "framework"
    ],
    
    "math_agent": [
        "math", "calculate", "equation", "formula", "solve", "computation",
        "probability", "statistics", "algebra", "geometry", "calculus",
        "number", "percentage", "average", "mean", "median", "sum"
    ]
}