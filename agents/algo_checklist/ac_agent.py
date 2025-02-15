
import os

from phoenix.agent import Agent
from phoenix.user_session import UserSession
from phoenix.models.azure_ai_inference import AzureAIInferece
import phoenix.models.openai_history as openai_history
from phoenix.connectors.mcp import MCPClient, MCPServer
from agents.utils import mcp_servers_path_getter

async def run():
    # Initialize chat history
    chat_history = openai_history.ChatHistory()

    # Setup LLM with Azure AI
    llm = AzureAIInferece(
        token=os.getenv("GITHUB_TOKEN"),
        history=chat_history,
        model=os.getenv("AI_MODEL"),
        temperature=0.1,
    )

    # Setup MCP connector with servers
    get = mcp_servers_path_getter("algo_checklist/servers")
    mcp = MCPClient([
        MCPServer(path=get("checklist.py"))
    ])

    try:
        await mcp.connect()

        system = """
You are an Algorithmic problems checklist holder assistant.
I have multiple problems to solve, and you will help me pick what to solve next based on my progress and priority.
You can also suggest insights into my solutions and provide feedback on my progress, if I ask you to.

Progress management is handled externally using the spec provided in this description.
"""

        # Create agent
        agent = Agent(
            brain=llm,
            history=chat_history,
            connector=mcp,
            system=system,
        )

        # Create user session and interact
        session = UserSession()

        while True:
            question = input("Q >> ")
            if not question:
                print("Please enter a valid question.")
                continue

            if question == "exit":
                break
            response = await agent.call(question, session)
            print(f"A >> {response}")

    finally:
        await mcp.cleanup()
