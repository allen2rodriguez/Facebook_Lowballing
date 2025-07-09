import subprocess # Use this to run ollama commands
# Consider making this into c++ (or equivalent) file to speed it up 
def aiResponse(webScrapedInfo: str) -> str:
    try:
        run_cold = subprocess.run(['ollama', 'run', 'lowballingAI', webScrapedInfo], 
                                  capture_output=True, 
                                  text=True,
                                  encoding='utf-8',
                                  errors='replace')
        ai_response = run_cold.stdout.strip()
        return ai_response
    except Exception as e:
        return None