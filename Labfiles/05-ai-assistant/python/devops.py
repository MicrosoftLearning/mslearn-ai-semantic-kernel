import os
import asyncio
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.functions.kernel_function_from_prompt import KernelFunctionFromPrompt
from semantic_kernel.connectors.ai.open_ai.prompt_execution_settings.azure_chat_prompt_execution_settings import (
    AzureChatPromptExecutionSettings,
)
from semantic_kernel.prompt_template.handlebars_prompt_template import HandlebarsPromptTemplate
from semantic_kernel.prompt_template.prompt_template_config import PromptTemplateConfig, InputVariable
from typing import Awaitable, Callable
from semantic_kernel.filters import FunctionInvocationContext
from semantic_kernel.functions import FunctionResult
from semantic_kernel.functions.kernel_function_decorator import kernel_function
from pathlib import Path

async def main():

    load_dotenv()
    # Set your values in the .env file
    api_key = os.getenv("AZURE_OPENAI_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("DEPLOYMENT_NAME")

    # Create a kernel builder with Azure OpenAI chat completion

    # Import plugins to the kernel
    
    # Add filters to the kernel
    
    # Create a kernel function to deploy the staging environment
    
    # Create a handlebars prompt
    
    # Create the prompt template config using handlebars format
    
    # Create a plugin function from the prompt

    # Create prompt execution settings

    # Create chat history

    # User interaction logic
    """
    async def get_reply():
        reply = await chat_completion.get_chat_message_content(
            chat_history=chat_history,
            kernel=kernel,
            settings=execution_settings
        )
        print("Assistant:", reply)
        chat_history.add_assistant_message(str(reply))

    def get_input():
        user_input = input("User: ")
        if user_input.strip() != "":
            chat_history.add_user_message(user_input)
        return user_input

    print("Press enter to exit")
    print("Assistant: How may I help you?")
    user_input = input("User: ")

    if user_input.strip() != "":
        chat_history.add_user_message(user_input)

    while user_input.strip() != "":
        await get_reply()
        user_input = get_input()
    """
    
# A class for Devops functions
class DevopsPlugin:
    """A plugin that performs developer operation tasks."""

    # Create a kernel function to build the stage environment

    
    @kernel_function(name="DeployToStage")
    def deploy_to_stage(self):
        return "Staging site deployed successfully."
    
    @kernel_function(name="DeployToProd")
    def deploy_to_prod(self):
        return "Production site deployed successfully."

    @kernel_function(name="CreateNewBranch")
    def create_new_branch(self, branchName: str, baseBranch: str):
        return f"Created new branch `{branchName}` from `{baseBranch}`."

    @kernel_function(name="CreateNewBranch")
    def create_new_branch(self, branchName: str, baseBranch: str):
        return f"Created new branch `{branchName}` from `{baseBranch}`."
    
    @kernel_function(name="ReadLogFile")
    def read_log_file(self):
        file_path = Path(__file__) / "Files"
        with open("Files/build.log", 'r', encoding='utf-8') as file:
            return file.read()

# Create a function filter

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())