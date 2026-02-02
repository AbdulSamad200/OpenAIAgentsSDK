import os
from dotenv import load_dotenv

from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, RunResult
from tools import calculator, text_summarizer, weather_fetcher, web_search

load_dotenv()

# Initialize external client
external_client: AsyncOpenAI = AsyncOpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Initialize LLM model
llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.0-flash"
)

# Create agent with all available tools
agent: Agent = Agent(
    name="Assistant",
    model=llm_model,
    tools=[calculator, text_summarizer, weather_fetcher, web_search]
)

def display_tool_usage(runner: RunResult):
    """Display which tools were used during the conversation."""
    if hasattr(runner, 'messages') and runner.messages:
        print("\n🔧 Tools Used:")
        print("=" * 50)
        
        tool_usage_found = False
        for message in runner.messages:
            if hasattr(message, 'tool_calls') and message.tool_calls:
                for tool_call in message.tool_calls:
                    tool_name = getattr(tool_call, 'function', {}).get('name', 'Unknown Tool')
                    print(f"  🛠️  {tool_name}")
                    tool_usage_found = True
        
        if not tool_usage_found:
            print("  ℹ️  No tools were used - response based on LLM knowledge only")
        
        print("=" * 50)

def interactive_mode():
    """Run the agent in interactive mode."""
    print("🤖 OpenAI Agents SDK - Interactive Mode")
    print("=" * 50)
    print("Ask me anything! I can help with:")
    print("  🧮 Mathematical calculations")
    print("  📝 Text summarization")
    print("  🌤️ Weather information")
    print("  🔍 Web searches")
    print("  💬 General questions")
    print("\nType 'quit', 'exit', or 'bye' to stop the conversation.")
    print("=" * 50)
    
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye', 'q']:
                print("\n👋 Goodbye! Thanks for using the OpenAI Agents SDK demo.")
                break
            
            if not user_input:
                print("Please enter a question or request.")
                continue
            
            # Run the agent
            print("\n🤖 Assistant: Thinking...")
            runner: RunResult = Runner.run_sync(
                starting_agent=agent,
                input=user_input
            )
            
            # Display the response
            print(f"\n🤖 Assistant: {runner.final_output}")
            
            # Show which tools were used
            display_tool_usage(runner)
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye! Thanks for using the OpenAI Agents SDK demo.")
            break
        except Exception as e:
            print(f"\n❌ Error: {str(e)}")
            print("Please try again with a different question.")

if __name__ == "__main__":
    interactive_mode()