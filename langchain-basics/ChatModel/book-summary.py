from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, load_prompt

model = ChatOllama(model="qwen3:0.6b")

template = load_prompt('book-summary.json')

# response = model.invoke(template.format(
#     book_input="The Great Gatsby",
#     length_input="Concise summary"
# ))
# print(response.content)

chain = template | model

response = chain.invoke({
    "book_input": "Psychology of Money",
    "length_input": "Medium summary"
})
print(response.content)