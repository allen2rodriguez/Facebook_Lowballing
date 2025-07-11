import subprocess # Use this to run ollama commands
import random
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

def selecting_personas (number_of_needed_personas: int) -> list:
    '''
    This function will select the personas that will be used to create a message
    Args:
        number_of_needed_personas (int): A number that indicates how many personas to select and therefore how many messages to create
    Returns: 
        list: The list of strings that are the selected personas
    '''
    da_personas = {
        0: "The E-Girl",
        1: "The Victim",
        2: "The Senior Shopper",
        3: "Prince Charming",
        4: "Mr. Hard 2 Get",
        5: "The Expert",
        6: "The Douche Bag",
        7: "The Student",
        8: "The Reseller",
        9: "The Collector"
    }
    return random.sample(list(da_personas.values()), number_of_needed_personas)