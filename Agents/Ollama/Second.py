import ollama

response = ollama.generate(model='llama3.2:1b', prompt='Tell me the story of Bhangardh fort, Arwal, Rajasthan', system='You are a storyteller.', stream=True)

for chunk in response:
    print(chunk['response'], end='', flush=True)