import os
import asyncio
from dotenv import load_dotenv

# Import namespaces



async def main():

    load_dotenv()
    # Set your values in the .env file
    api_key = os.getenv("AZURE_OPENAI_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("DEPLOYMENT_NAME")


    # Create a kernel with Azure OpenAI chat completion
    

    # Test the chat completion service

if __name__ == "__main__":
        asyncio.run(main())