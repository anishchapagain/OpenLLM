import openai
import os
from openai import OpenAI

openai.api_key = os.getenv('OPENAIAPI')
client = OpenAI()

# find_city_text = "Balen lives in Rio.; Peter in Guyana.; Peter is currently living in St Louis." # test
# user_prompt = "Where does Peter live?"
user_prompt = "Where does Peter live?\nBalen lives in Rio.; Peter was living in Guyana.; Peter is currently living in St Louis."

response = client.chat.completions.create(
  model='gpt-3.5-turbo', 
  messages=[
    {"role": "user", 
     "content": user_prompt
    }
  ]
)

"""
response = openai.Completion.create(
  engine="davinci", # Abstract  engine="text-davinci-003",  
  prompt=prompt, 
  max_tokens=50
)
"""
# print(response['choices'][0]['text'].strip())
print(response.choices[0].message.content)
