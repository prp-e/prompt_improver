from openai import OpenAI
from config import * 

client = OpenAI(api_key = OPENAI_API_KEY, base_url = OPENAI_ENDPOINT)

def improver(prompt):
    
    client.chat.completions.create()

if __name__ == "__main__":
    while True:
        user_input = input("Enter your desired system prompt (or input \"exit\" to exit.): ")
        if user_input == "exit":
            break
