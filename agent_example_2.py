from langchain.llms import Ollama
from langchain.agents import load_tools, initialize_agent, AgentType
import os

# Set up the SerpAPI key
os.environ["SERPAPI_API_KEY"] = "your_serpapi_api_key"

# Initialize the Ollama LLM
llm = Ollama(model="llama3.2:1b")  # Ensure the model is accessible via Ollama

# Load tools
tools = load_tools(["serpapi", "llm-math"], llm=llm)

# Define the agent with a custom prompt template and retry limits
template = """
You are an AI assistant. Follow this structured reasoning process to solve problems:
1. Thought: Explain your reasoning.
2. Action: Specify the tool to use (e.g., `search` or `calculator`).
3. Action Input: Provide the input for the action.

Question: {input}
{agent_scratchpad}
"""

# Initialize an agent with tools, LLM, and limits
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    max_iterations=3,  # Limits retries
)

# Run the agent
try:
    response = agent.run("Who is Olivia Wilde's boyfriend?")
    print("Response:", response)
except Exception as e:
    print(f"Error: {e}")
