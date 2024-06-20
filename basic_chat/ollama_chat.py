import ollama
response = ollama.chat(model='llama3', messages=[
  {
    'role': 'user',
    'content': 'Oi, tudo bem?',
  },
])
print(response['message']['content'])