import ollama

response = ollama.generate(model='llama3.2:1b', prompt= 'Who is the Prime minister of the India?', stream=True)

for chunk in response:
    print(chunk['response'], end='', flush=True)

