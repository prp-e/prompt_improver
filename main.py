from openai import OpenAI
from config import * 

client = OpenAI(api_key = OPENAI_API_KEY, base_url = OPENAI_ENDPOINT)

prompt = open('prompt.md')
prompt = prompt.read()

def improver(prompt):

    completion = client.chat.completions.create(
        model = "openai",
        messages = [
            {
                "role" : "user",
                "content" : f"improve my prompt: {prompt}"
            }
        ]
    )

    return completion.choices[0].message.content

if __name__ == "__main__":
    while True:
        user_input = input("Enter your desired system prompt (or input \"exit\" to exit.): ")

        if user_input == "exit":
            break

        improved_prompt = improver(user_input)
        print("wait...")
        print(improved_prompt)
