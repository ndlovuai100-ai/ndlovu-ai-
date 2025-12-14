# Registry for Ndlovu AI agents

agents = {}

def register_agent(name, role_description):
    agents[name] = role_description
    print(f"Agent '{name}' registered with role: {role_description}")

# Register core agents
register_agent("Nkhudu", "Core executor and system manager")
register_agent("Kamara", "Strategist and oracle logic")
register_agent("Assistant", "Supportive reasoning and memory handler")
