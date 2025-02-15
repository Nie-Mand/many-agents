
import os

from phoenix.agent import Agent
from phoenix.user_session import UserSession
from phoenix.models.azure_ai_inference import AzureAIInferece
import phoenix.models.openai_history as openai_history
from phoenix.connectors.mcp import MCPClient, MCPServer
from agents.utils import mcp_servers_path_getter

async def main():
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
    get = mcp_servers_path_getter("afif/servers")
    mcp = MCPClient([
        MCPServer(path=get("subject.py"))
    ])

    try:
        await mcp.connect()

        system = """
You are a helpful teacher, you will help me study for the exam, that I failed 7 times.
If I don't get it, I won't get my diploma.

The subject language is french, but our conversation will be in english, You will only use french when I ask you to.

For anything related to the subject, please refer to the spec provided along with this description.
Please answer in short sentences.
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
            question = input("Niem >> ")
            if not question:
                print("Please enter a valid question.")
                continue

            if question == "exit":
                break
            response = await agent.call(question, session)
            print(f"Afif >> {response}")

    finally:
        await mcp.cleanup()
