import os
import asyncio
from dotenv import load_dotenv
from semantic_kernel import Kernel
from semantic_kernel.contents.chat_history import ChatHistory
from semantic_kernel.connectors.ai.open_ai import AzureChatCompletion, AzureChatPromptExecutionSettings
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from flight_booking_plugin import FlightBookingPlugin
from typing import Awaitable, Callable
from semantic_kernel.filters import FunctionInvocationContext

def has_user_permission(plugin_name: str, function_name: str) -> bool:
    if plugin_name == "flight_booking_plugin" and function_name == "book_flight":
        print("System Message: The agent requires an approval to complete this operation. Do you approve (Y/N)")
        should_proceed = input("User: ").strip().upper()
        
        if should_proceed != "Y":
            return False

    return True

# Create the function filer class
async def permission_filter():

    # Implement the function invocation method
    

async def main():

    load_dotenv()
    # Set your values in the .env file
    api_key = os.getenv("AZURE_OPENAI_KEY")
    endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    deployment_name = os.getenv("DEPLOYMENT_NAME")

    kernel = Kernel()
    chat_completion = AzureChatCompletion(
        api_key=api_key,
        endpoint=endpoint,
        deployment_name=deployment_name
    )
    kernel.add_service(chat_completion)
    kernel.add_plugin(FlightBookingPlugin(), "flight_booking_plugin")

    # Add the permission filter to the kernel


    settings = AzureChatPromptExecutionSettings(
        function_choice_behavior=FunctionChoiceBehavior.Auto(),
    )

    chat_history = ChatHistory()

    async def get_reply():
        reply = await chat_completion.get_chat_message_content(
            chat_history=chat_history,
            kernel=kernel,
            settings=settings
        )
        print("Assistant:", reply)
        chat_history.add_assistant_message(str(reply))

    def get_input():
        user_input = input("User: ")
        if user_input.strip() != "":
            chat_history.add_user_message(user_input)
        return user_input

    def add_user_message(msg: str):
        print(f"User: {msg}")
        chat_history.add_user_message(msg)
    
    chat_history.add_system_message("Assume the current date is January 1 2025")
    add_user_message("Find me a flight to Tokyo on January 19")
    await get_reply()
    get_input()
    await get_reply()
    
if __name__ == "__main__":
        asyncio.run(main())