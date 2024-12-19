from openai import OpenAI
from config import * 

client = OpenAI(api_key = OPENAI_API_KEY, base_url = OPENAI_ENDPOINT)

def improver(prompt):
    pass