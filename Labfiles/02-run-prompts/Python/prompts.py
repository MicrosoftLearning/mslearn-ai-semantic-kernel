import os
import asyncio
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.functions.kernel_arguments import KernelArguments
from semantic_kernel.prompt_template import KernelPromptTemplate, HandlebarsPromptTemplate, PromptTemplateConfig

async def main():

    load_dotenv()
    # Set your values in the .env file
    api_key = os.getenv("AZURE_OPENAI_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("DEPLOYMENT_NAME")

    # Create a kernel with Azure OpenAI chat completion
   

    # Create the chat history
    

    async def get_reply():
        # Get the reply from the chat completion service
        

    # Create a semantic kernel prompt template
    

    # Render the Semantic Kernel prompt with arguments
    

    # Add the Semantic Kernel prompt to the chat history and get the reply
    

    # Create a handlebars template
    

    # Render the Handlebars prompt with arguments
    

    # Add the Handlebars prompt to the chat history and get the reply
    

    # Get a follow-up prompt from the user
    

    # Add the user input to the chat history and get the reply


if __name__ == "__main__":
        asyncio.run(main())