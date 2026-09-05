from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain.agents import create_agent
from langchain_core.messages import HumanMessage

model = ChatOllama(
    model="qwen3:8b",
    temperature=0.3
)

users = {
    1: {"name": "John", "role": "admin"},
    2: {"name": "Mike", "role": "user"}
}

@tool
def get_user_by_id(user_id: int):
    """
    Get user information by user ID.
    """
    return users.get(user_id, "User not found.")

question = "What is the name of the user with ID 1?"

tools = [get_user_by_id]

agent = create_agent(
    model=model,
    tools=tools,
    system_prompt=(
        "You are a helpful assistant. "
        "Use the get_user_by_id tool when the user asks "
        "for user information."
    )
)

result = agent.invoke({
    "messages": [
        {
            "role": "user",
            "content": question
        }
    ]
})

print(result["messages"][-1].content)