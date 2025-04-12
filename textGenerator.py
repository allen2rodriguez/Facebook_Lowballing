import subprocess # Use this to run ollama commands

def coldAI(input):
    run_cold = subprocess.run(['ollama', 'run', 'cold', input], capture_output=True, text=True)
    cold_response = run_cold.stdout.strip()
    return cold_response

def doucheAI(input):
    run_cold = subprocess.run(['ollama', 'run', 'douche', input], capture_output=True, text=True)
    douche_response = run_cold.stdout.strip()
    return douche_response

# More bots soon to come