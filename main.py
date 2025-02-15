from dotenv import load_dotenv
import asyncio
import agents.afif.agent as afif

load_dotenv()

def main():
    asyncio.run(afif.main())

if __name__ == "__main__":
    main()
