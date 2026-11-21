from langchain_ollama import ChatOllama
from langchain.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

# 1. Initialize LLM
llm = ChatOllama(
    model="qwen3:0.6b",
    temperature=0
)

# 2. Create tools
@tool
def calculate_total(quantity: int, price: float) -> float:
    """Calculate total price using quantity and unit price."""
    return round(quantity * price, 2)

@tool
def apply_discount(amount: float, discount_percentage: float) -> float:
    """Apply percentage discount to the given amount."""
    discount = amount * discount_percentage / 100
    return round(amount - discount, 2)

@tool
def add_delivery(amount: float, delivery_charge: float) -> float:
    """Add delivery charges to the given amount."""
    return round(amount + delivery_charge, 2)

# 3. Register all tools
tools = [
    calculate_total,
    apply_discount,
    add_delivery
]

tool_with_name = {
    tool.name: tool for tool in tools
}

query = input("Please enter your question. \n")

message = [HumanMessage(content=query)]

llm_with_tool = llm.bind_tools(tools)

max_iter = 10

for i in range(max_iter):

    llm_response = llm_with_tool.invoke(message)

    print(f"llm response {llm_response}")

    message.append(llm_response)

    if not llm_response.tool_calls:
    
            print("\nFinal Answer:")
            print(llm_response.content)
            break

    for tool_call in llm_response.tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        print(f"\nExecuting Tool: {tool_name}")
        print(f"Arguments: {tool_args}")

        # Dynamically find the requested tool
        selected_tool = tool_with_name.get(tool_name)

        tool_call_response = selected_tool.invoke(tool_args)

        print(f"Tool call response {tool_call_response}")

        message.append(
            ToolMessage(
                content=str(tool_call_response),
                tool_call_id=tool_call["id"]
            )
        )