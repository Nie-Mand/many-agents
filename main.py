from dotenv import load_dotenv
import asyncio
from agents.afif import afif_agent
from agents.algo_checklist import ac_agent

load_dotenv()

def main():
    asyncio.run(ac_agent.run())

if __name__ == "__main__":
    main()
