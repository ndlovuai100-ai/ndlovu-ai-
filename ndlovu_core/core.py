
from ndlovu_core.registry import agents
import json
from ndlovu_core.config import DATA_PATH

def log_command(command, agent=None):
    # Load existing state
    try:
        with open(DATA_PATH, 'r') as f:
            state = json.load(f)
    except FileNotFoundError:
        state = {"commands_executed": [], "agent_memory": {}}

    # Log command
    entry = {"command": command, "agent": agent}
    state["commands_executed"].append(entry)

    # Save state
    with open(DATA_PATH, 'w') as f:
        json.dump(state, f, indent=2)

def route_command(command):
    """
    Simple routing logic:
    - Commands containing 'plan', 'strategy', 'oracle' -> Kamara
    - Commands containing 'execute', 'run', 'system' -> Nkhudu
    - Default -> Assistant
    """
    cmd_lower = command.lower()
    if any(word in cmd_lower for word in ["plan", "strategy", "oracle"]):
        return "Kamara"
    elif any(word in cmd_lower for word in ["execute", "run", "system"]):
        return "Nkhudu"
    else:
        return "Assistant"

def start_ndlovu():
    print("🐘 Ndlovu AI online.")
    print("Loaded Agents:", ", ".join(agents.keys()))
    print("Type 'exit' to shut down.")

    while True:
        command = input("ndlovu> ").strip()

        if command.lower() == "exit":
            print("Ndlovu AI shutting down.")
            break
        elif command == "":
            continue
        else:
            # Route command to appropriate agent
            agent = route_command(command)
            print(f"{agent} received command: {command}")
            log_command(command, agent)
