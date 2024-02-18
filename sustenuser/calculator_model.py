from monsterapi import client
import os
os.environ["MONSTER_API_KEY"] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjFhYmNhM2QwNTU2ZjIyNDc0NmEyZTdlMjFlNDA5YmIxIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDItMThUMDA6NDE6MzUuMzM5NDcwIn0.qpKVXWmP-sTizQH3dI7bekI-CLBShLLiDefTxAaEsUg"
client = client() # Initialize client

url = "https://api.monsterapi.ai/v1/generate/codellama-13b-instruct"

def calculate_score(text,historical_context):
    historical_context_stringified = '\n'.join(list(historical_context))
    print("\n\n\n",historical_context_stringified)
    text_request =  "Analyze the historical context from the following messages:- " + \
                historical_context_stringified + \
                "Now I want you to categorize the user's intent as [1] travelling via a " + \
                "mode of transport [2] eating something [3] or [0] none of the above. " + \
                "Return an empty string if none of these actions are identified." + \
                "For each identified action, output its category number enclosed in square brackets, " + \
                "followed by a comma and a single-digit score reflecting sustainability (1-10, with 1 being "+ \
                "the least sustainable and 10 the most sustainable and making sure each number " + \
                "is equally probable). Separate each identified action with a newline. "+ \
                "Focus only on actions that are explicitly mentioned in the text. " + \
                "ONLY GIVE THE DESCRIBED NUMBERS, ABSOLUTELY NO TEXT! CONTEXT: " + text
    result = client.generate(
        model='codellama-13b-instruct', data={
        "beam_size": 1,
        "max_length": 20,
        "prompt": text_request,
        "system"
        "temp": 0.2,
        "top_k": 20,
        "top_p": 0.5
    })
    print("calculator_model.response=",result)
    return result