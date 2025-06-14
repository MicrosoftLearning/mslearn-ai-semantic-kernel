using Microsoft.Extensions.Configuration;
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.ChatCompletion;
using Microsoft.SemanticKernel.Connectors.OpenAI;
using Microsoft.SemanticKernel.PromptTemplates.Handlebars;

string filePath = Path.GetFullPath("appsettings.json");
var config = new ConfigurationBuilder()
    .AddJsonFile(filePath)
    .Build();

// Set your values in appsettings.json
string apiKey = config["PROJECT_KEY"]!;
string endpoint = config["PROJECT_ENDPOINT"]!;
string deploymentName = config["DEPLOYMENT_NAME"]!;

// Create a kernel with Azure OpenAI chat completion


// Create the chat history


// Create a semantic kernel prompt template


// Render the Semantic Kernel prompt with arguments


// Add the Semanitc Kernel prompt to the chat history and get the reply


// Create a handlebars template


// Render the Handlebars prompt with arguments


// Add the Handlebars prompt to the chat history and get the reply


// Get a follow-up prompt from the user


// Add the user input to the chat history and get the reply


async Task GetReply() {
    // Get the reply from the chat completion service
    
}