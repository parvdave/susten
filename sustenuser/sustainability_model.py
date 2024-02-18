from monsterapi import client
import os
os.environ["MONSTER_API_KEY"] = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6IjFhYmNhM2QwNTU2ZjIyNDc0NmEyZTdlMjFlNDA5YmIxIiwiY3JlYXRlZF9hdCI6IjIwMjQtMDItMThUMDA6NDE6MzUuMzM5NDcwIn0.qpKVXWmP-sTizQH3dI7bekI-CLBShLLiDefTxAaEsUg"
client = client() # Initialize client
url = "https://ad19a9ca-774e-4776-9ddf-5ebd48d406dd.monsterapi.ai"
# text = "I am going to work by car because no bus is available. Is this ok? I literally do not have any other option!"

def generate_response(text):
    result = client.generate(model='codellama-13b-instruct', data={
        "beam_size": 1,
        "max_length": 300,
        "prompt": "Answer this prompt, argue the most sustainable options (but do not mention this request in the response): " + text,
        "repetition_penalty": 1.2,
        "system_prompt": "Give the user information on how they can be sustainable given their prompt. Provide alternatives to non-sustainable actions, focus on sustainability and mention it as much as possible (if not possible reassure the interlocutor).",
        "temp": 0.8,
        "top_k": 40,
        "top_p": 1
    })
    print(result)
    return result
