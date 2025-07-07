import subprocess # Use this to run ollama commands
# Consider making this into c++ (or equivalent) file to speed it up 
def aiResponse(input, ai_name):
    try:
        run_cold = subprocess.run(['ollama', 'run', ai_name, input], 
                                  capture_output=True, 
                                  text=True,
                                  encoding='utf-8',
                                  errors='replace')
        ai_response = run_cold.stdout.strip()
        return ai_response
    except Exception as e:
        print(f"Error with {ai_name}: {e}")
        return None