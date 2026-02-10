from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent 


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

def isprime(num: int) -> str:
    """Check if a number is prime."""
    for i in range(2, num):
        if num % i == 0:
            return "Not Prime"
    return "Prime"

model = ChatGoogleGenerativeAI(
    model="gemini-3-flash-preview",
    temperature=1.0,
)

agent = create_agent(
    model=model,
    tools=[get_weather,isprime],
    system_prompt="You are a helpful assistant",
)

# Run the agent
response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in mysore and is 2001 prime?"}]}
)

# Print only the final AI response
final_msg = response["messages"][-1]
if isinstance(final_msg.content, list):
    for block in final_msg.content:
        if isinstance(block, dict) and block.get("type") == "text":
            print(block["text"])
else:
    print(final_msg.content)