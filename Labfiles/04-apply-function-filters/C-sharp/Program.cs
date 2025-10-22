using Microsoft.Extensions.Configuration;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;

string filePath = Path.GetFullPath("appsettings.json");
var config = new ConfigurationBuilder()
    .AddJsonFile(filePath)
    .Build();

// Set your values in appsettings.json
string apiKey = config["AZURE_OPENAI_KEY"]!;
string endpoint = config["AZURE_OPENAI_ENDPOINT"]!;
string deploymentName = config["DEPLOYMENT_NAME"]!;

// Create a kernel with Azure OpenAI chat completion
var builder = Kernel.CreateBuilder();
builder.AddAzureOpenAIChatCompletion(deploymentName, endpoint, apiKey);
OpenAIPromptExecutionSettings openAIPromptExecutionSettings = new() 
{
    FunctionChoiceBehavior = FunctionChoiceBehavior.Auto(),
};

var kernel = builder.Build();
kernel.Plugins.AddFromType<FlightBookingPlugin>("FlightBookingPlugin");

// Add the permission filter to the kernel


var chatCompletionService = kernel.GetRequiredService<IChatCompletionService>();
var history = new ChatHistory();

history.AddSystemMessage("Assume the current date is January 1 2025");
AddUserMessage("Find me a flight to Tokyo on the 19");
await GetReply();
GetInput();
await GetReply();

void GetInput() {
    Console.Write("User: ");
    string input = Console.ReadLine()!;
    history.AddUserMessage(input);
}

async Task GetReply() {
    ChatMessageContent reply = await chatCompletionService.GetChatMessageContentAsync(
        history,
        executionSettings: openAIPromptExecutionSettings,
        kernel: kernel
    );
    Console.WriteLine("Assistant: " + reply.ToString());
    history.AddAssistantMessage(reply.ToString());
}

void AddUserMessage(string msg)
{
    Console.WriteLine("User: " + msg);
    history.AddUserMessage(msg);
}

// Create the function filer class
public class PermissionFilter
{

    // Implement the function invocation method
    

    private Boolean HasUserPermission(string pluginName, string functionName)
    {
        if (pluginName.Equals("FlightBookingPlugin") && functionName.Equals("book_flight"))
        {
            Console.WriteLine("System Message: The agent requires an approval to complete this operation. Do you approve (Y/N)");
            Console.Write("User: ");
            string shouldProceed = Console.ReadLine()!;

            if (shouldProceed != "Y")
            {
                return false;
            }
        }

        return true;
    }
}