using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;
using Microsoft.Extensions.Configuration;
using Microsoft.SemanticKernel.PromptTemplates.Handlebars;

string filePath = Path.GetFullPath("appsettings.json");
var config = new ConfigurationBuilder()
.AddJsonFile(filePath)
.Build();

// Set your values in appsettings.json
string apiKey = config["AZURE_OPENAI_KEY"]!;
string endpoint = config["AZURE_OPENAI_ENDPOINT"]!;
string deploymentName = config["DEPLOYMENT_NAME"]!;

// Create a kernel builder with Azure OpenAI chat completion

// Import plugins to the kernel

// Create prompt execution settings

// Create chat history

// Create a kernel function to deploy the staging environment

// Create a handlebars prompt

// Create the prompt template config using handlebars format

// Create a plugin function from the prompt

// Add filters to the kernel

Console.WriteLine("Press enter to exit");
Console.WriteLine("Assistant: How may I help you?");
Console.Write("User: ");

string input = Console.ReadLine()!;

// User interaction logic
/*
while (input != "") 
{
    chatHistory.AddUserMessage(input);
    await GetReply();
    input = GetInput();
}

string GetInput() 
{
    Console.Write("User: ");
    string input = Console.ReadLine()!;
    chatHistory.AddUserMessage(input);
    return input;
}

async Task GetReply() 
{
    ChatMessageContent reply = await chatCompletionService.GetChatMessageContentAsync(
        chatHistory,
        executionSettings: openAIPromptExecutionSettings,
        kernel: kernel
    );
    Console.WriteLine("Assistant: " + reply.ToString());
    chatHistory.AddAssistantMessage(reply.ToString());
}
*/

class DevopsPlugin
{
    // Create a kernel function to build the stage environment
    
    [KernelFunction("DeployToStage")]
    public string DeployToStage()
    {
        return "Staging site deployed successfully.";
    }

    [KernelFunction("DeployToProd")]
    public string DeployToProd() 
    {
        return "Production site deployed successfully.";
    }

    [KernelFunction("CreateNewBranch")]
    public string CreateNewBranch(string branchName, string baseBranch) {
        return $"Created new branch `{branchName}` from `{baseBranch}`";
    }

    [KernelFunction("ReadLogFile")]
    public string ReadLogFile() 
    {
        string content = File.ReadAllText($"Files/build.log");
        return content;
    }
}

// Create a function filter
