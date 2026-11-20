
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

# Create tool lookup dictionary
tools_by_name = {
    tool.name: tool for tool in tools
}


# 4. Bind tools with LLM
llm_with_tools = llm.bind_tools(tools)


# 5. Prepare conversation
messages = [
    HumanMessage(
        content="""
        Calculate the shopping bill.

        Requirements:
        1. Calculate total for 3 products costing 500 each.
        2. Apply a 10% discount to the total.
        3. Add 50 delivery charges to the discounted amount.

        Call one tool at a time.
        Wait for its result before selecting the next tool.
        Follow the steps in the given order.
        """
    )
]


# 6. Execute agent/tool calling loop
max_iterations = 10

for step in range(max_iterations):

    # Ask LLM what to do next
    response = llm_with_tools.invoke(messages)

    # Add LLM response to conversation history
    messages.append(response)

    # Check whether LLM requested a tool
    if not response.tool_calls:

        print("\nFinal Answer:")
        print(response.content)
        break

    # Execute requested tools
    for tool_call in response.tool_calls:

        tool_name = tool_call["name"]
        tool_args = tool_call["args"]

        print(f"\nExecuting Tool: {tool_name}")
        print(f"Arguments: {tool_args}")

        # Dynamically find the requested tool
        selected_tool = tools_by_name.get(tool_name)

        if selected_tool is None:
            result = f"Error: Unknown tool {tool_name}"
        else:
            try:
                # Execute the selected tool
                result = selected_tool.invoke(tool_args)
            except Exception as error:
                result = f"Tool execution failed: {error}"

        print(f"Tool Result: {result}")

        # Send tool result back to LLM
        messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"]
            )
        )

else:
    print("Maximum tool execution steps reached.")
