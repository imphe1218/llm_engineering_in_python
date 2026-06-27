from dotenv import load_dotenv
from bs4 import BeautifulSoup
from openai import OpenAI

openai = OpenAI(base_url="http://localhost:11434/v1", api_key="ollama")

message = "say hello world for me Ollama!"
response = openai.chat.completions.create(model="llama3.2", messages=[{"role":"user", "content":message}])
print(response.choices[0].message.content)