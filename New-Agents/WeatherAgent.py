from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
# from langchain.agents import create_agent


# --------------------------------------------------
# 1. Create the LLM
# --------------------------------------------------

model = ChatOllama(
    model="qwen3:8b",
    temperature=0
)


# --------------------------------------------------
# 2. Create a tool
# --------------------------------------------------

@tool
def get_weather(city: str) -> str:
    """Get the weather for a city."""
    
    weather_data = {
        "delhi": "Hot and sunny, 38°C",
        "mumbai": "Humid and cloudy, 31°C",
        "bangalore": "Pleasant and cloudy, 24°C",
        "pune": "Partly cloudy, 27°C"
    }

    return weather_data.get(
        city.lower(),
        f"Weather data for {city} is not available."
    )


# --------------------------------------------------
# 3. Give tools to the agent
# --------------------------------------------------

tools = [get_weather]


# --------------------------------------------------
# 4. Create the agent
# --------------------------------------------------

# agent = create_agent(
#     model=model,
#     tools=tools,
#     system_prompt=(
#         "You are a helpful assistant. "
#         "Use the weather tool when the user asks about weather."
#     )
# )

model_with_tool = model.bind_tools(tools)


# --------------------------------------------------
# 5. Ask the agent a question
# --------------------------------------------------

# result = agent.invoke({
#     "messages": [
#         {
#             "role": "user",
#             "content": "What is the weather in Bangalore?"
#         }
#     ]
# })

query = HumanMessage('What is the weather in Bangalore?')

messages = [query]

result = model_with_tool.invoke(messages)


# --------------------------------------------------
# 6. Print the final response
# --------------------------------------------------
print(result)
# print(result['tool_calls'][0])
# print(result["messages"][-1].content)

tool_call = result.tool_calls[0]

tool_result = get_weather.invoke(
    tool_call["args"]
)

print(tool_result)
