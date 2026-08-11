from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOllama(model="qwen3:0.6b")

template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)

parser = StrOutputParser()

chain = template1 | model | parser | template2 | model | parser

def validate_topic(topic):
    topic = topic.strip()

    # 1. Empty input
    if not topic:
        return False, "Topic cannot be empty."

    # 2. Minimum length
    if len(topic) < 3:
        return False, "Topic must contain at least 3 characters."

    # 3. Maximum length
    if len(topic) > 100:
        return False, "Topic cannot exceed 100 characters."

    # 4. Check if input contains at least one alphabet
    if not any(char.isalpha() for char in topic):
        return False, "Please enter a valid topic containing letters."

    # 5. Block unwanted topics
    blocked_words = ["hack", "password", "malware"]

    for word in blocked_words:
        if word.lower() in topic.lower():
            return False, f"The topic contains a restricted word: {word}"

    return True, topic

while True:

    user_input = input("Enter a topic: \n")

    is_valid, message = validate_topic(user_input)

    if is_valid:
        user_input = message
        break

    print(f"❌ Invalid input: {message}")
    print("Please try again.\n")



result = chain.invoke({'topic':user_input})

print(result)
