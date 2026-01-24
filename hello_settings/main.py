import os
from dotenv import load_dotenv

from agents import Agent, Runner, function_tool, ModelSettings, OpenAIChatCompletionsModel, AsyncOpenAI, set_tracing_disabled

# 🌿 Load environment variables from .env file
load_dotenv()

# 🚫 Disable tracing for clean output (optional for beginners)
set_tracing_disabled(disabled=True)

# 🔐 1) Environment & Client Setup
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")  # 🔑 Get your API key from environment
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")  # 🔑 Get your OpenAI API key from environment
BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"  # 🌐 Gemini-compatible base URL (set this in .env file)

# 🌐 Initialize clients for both Gemini and OpenAI
gemini_client: AsyncOpenAI = AsyncOpenAI(api_key=GEMINI_API_KEY, base_url=BASE_URL)
openai_client: AsyncOpenAI = AsyncOpenAI(api_key=OPENAI_API_KEY)

# 🧠 2) Model Initialization
gemini_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(model="gemini-2.5-flash", openai_client=gemini_client)
openai_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(model="gpt-4o-mini", openai_client=openai_client)

# 🛠️ Tools for learning
@function_tool
def calculate_area(length: float, width: float) -> str:
    """Calculate the area of a rectangle."""
    area = length * width
    return f"Area = {length} × {width} = {area} square units"

@function_tool
def get_weather(city: str) -> str:
    """Get weather information for a city."""
    # Simulated weather data
    weather_data = {
        "New York": "Sunny, 22°C",
        "London": "Cloudy, 15°C", 
        "Tokyo": "Rainy, 18°C",
        "Paris": "Partly cloudy, 20°C"
    }
    return f"Weather in {city}: {weather_data.get(city, 'Weather data not available')}"

@function_tool
def calculate_math(expression: str) -> str:
    """Calculate a mathematical expression safely."""
    try:
        # Simple safe evaluation for basic math
        allowed_chars = set('0123456789+-*/.() ')
        if all(c in allowed_chars for c in expression):
            result = eval(expression)
            return f"{expression} = {result}"
        else:
            return "Invalid expression. Only numbers and basic operators allowed."
    except:
        return "Error calculating expression."

@function_tool
def translate_text(text: str, language: str) -> str:
    """Translate text to a specified language."""
    # Simulated translation
    translations = {
        "spanish": f"Spanish: {text} (translated)",
        "french": f"French: {text} (translated)", 
        "german": f"German: {text} (translated)",
        "italian": f"Italian: {text} (translated)"
    }
    return translations.get(language.lower(), f"Translation to {language}: {text}")

def main():
    """Learn Model Settings with simple examples."""
    # 🎯 Example 1: Temperature (Creativity Control)
    print("\n❄️🔥 Temperature Settings")
    print("-" * 30)
    
    agent_cold = Agent(
        name="Cold Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=0.1),
        model=gemini_model
    )
    
    agent_hot = Agent(
        name="Hot Agent",
        instructions="You are a helpful assistant.",
        model_settings=ModelSettings(temperature=1.9),
        model=gemini_model
    )
    
    question = "Tell me about AI in 2 sentences"
    
    print("Cold Agent (Temperature = 0.1):")
    result_cold = Runner.run_sync(agent_cold, question)
    print(result_cold.final_output)
    
    print("\nHot Agent (Temperature = 1.9):")
    result_hot = Runner.run_sync(agent_hot, question)
    print(result_hot.final_output)
    
    print("\n💡 Notice: Cold = focused, Hot = creative")
    print("📝 Note: Gemini temperature range extends to 2.0")
    
    # 🎯 Example 2: Tool Choice
    print("\n🔧 Tool Choice Settings")
    print("-" * 30)
    
    agent_auto = Agent(
        name="Auto",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="auto"),
        model=gemini_model
    )
    
    agent_required = Agent(
        name="Required",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="required"),
        model=gemini_model
    )

    agent_none = Agent(
        name="None",
        tools=[calculate_area],
        model_settings=ModelSettings(tool_choice="none"),
        model=gemini_model
    )
    
    question = "What's the area of a 5x3 rectangle?"
    
    print("Auto Tool Choice:")
    result_auto = Runner.run_sync(agent_auto, question)
    print(result_auto.final_output)
    
    print("\nRequired Tool Choice:")
    result_required = Runner.run_sync(agent_required, question)
    print(result_required.final_output)

    print("\nNone Tool Choice:")
    result_none = Runner.run_sync(agent_none, question)
    print(result_none.final_output)
    
    print("\n💡 Notice: Auto = decides, Required = must use tool")
    
    # 🎯 Example 3: Multi-Tool Usage with Gemini
    print("\n🛠️ Multi-Tool Usage (Gemini)")
    print("-" * 35)
    
    # Agent with multiple tools (sequential by default for Gemini)
    multi_tool_agent = Agent(
        name="Multi-Tool Agent",
        tools=[get_weather, calculate_math, translate_text],
        model_settings=ModelSettings(
            tool_choice="auto"
        ),
        model=gemini_model
    )
    
    # Test multi-tool usage
    multi_task_question = "What's the weather in New York, calculate 15 * 8, and translate 'Hello' to Spanish"
    
    print("🛠️ Multi-Tool Agent (Gemini - sequential):")
    result_multi = Runner.run_sync(multi_tool_agent, multi_task_question)
    print(result_multi.final_output)
    
    print("\n💡 Notice: Gemini uses tools sequentially (one after another)")
    
    # 🎯 Example 4: Parallel Tool Calls with OpenAI
    print("\n⚡ Parallel Tool Calls (OpenAI)")
    print("-" * 35)
    
    # Agent that can use multiple tools simultaneously (OpenAI)
    parallel_agent = Agent(
        name="Parallel Agent",
        tools=[get_weather, calculate_math, translate_text],
        model_settings=ModelSettings(
            tool_choice="auto",
            parallel_tool_calls=True  # Multiple tools simultaneously
        ),
        model=openai_model
    )
    
    # Agent that uses tools one at a time (OpenAI)
    sequential_agent = Agent(
        name="Sequential Agent",
        tools=[get_weather, calculate_math, translate_text],
        model_settings=ModelSettings(
            tool_choice="auto",
            parallel_tool_calls=False  # One tool at a time
        ),
        model=openai_model
    )
    
    print("🔄 Sequential Agent (OpenAI - one tool at a time):")
    result_sequential = Runner.run_sync(sequential_agent, multi_task_question)
    print(result_sequential.final_output)
    
    print("\n⚡ Parallel Agent (OpenAI - multiple tools simultaneously):")
    result_parallel = Runner.run_sync(parallel_agent, multi_task_question)
    print(result_parallel.final_output)
    
    print("\n💡 Notice:")
    print("• Sequential = tools called one after another")
    print("• Parallel = multiple tools called simultaneously (faster)")
    print("• Parallel tool calls only work with OpenAI models")
    
    # 🎯 Example 5: Advanced Model Settings (OpenAI)
    print("\n🎛️ Advanced Model Settings (OpenAI)")
    print("-" * 40)
    
    # High creativity agent with advanced settings
    creative_agent = Agent(
        name="Creative",
        model_settings=ModelSettings(
            temperature=1.5,
            top_p=0.9,
            frequency_penalty=0.8,
            presence_penalty=0.6,
        ),
        model=openai_model
    )
    
    # Conservative agent with controlled settings
    conservative_agent = Agent(
        name="Conservative",
        model_settings=ModelSettings(
            temperature=0.2,
            top_p=0.5,
            frequency_penalty=0.1,
            presence_penalty=0.1
        ),
        model=openai_model
    )
    
    # Focused agent with parallel tool calls
    focused_parallel_agent = Agent(
        name="Focused Parallel",
        tools=[get_weather, calculate_math, translate_text],
        model_settings=ModelSettings(
            tool_choice="auto",
            parallel_tool_calls=True,
            top_p=0.3,              # Use only top 30% of vocabulary
            frequency_penalty=0.5,   # Avoid repeating words
            presence_penalty=0.3     # Encourage new topics
        ),
        model=openai_model
    )
    
    creative_question = "Write a short creative story about a robot learning to paint"
    
    print("🎨 Creative Agent (high creativity settings):")
    result_creative = Runner.run_sync(creative_agent, creative_question)
    print(result_creative.final_output)
    
    print("\n📝 Conservative Agent (low creativity settings):")
    result_conservative = Runner.run_sync(conservative_agent, creative_question)
    print(result_conservative.final_output)
    
    print("\n🎯 Focused Parallel Agent (parallel tools + controlled vocabulary):")
    result_focused_parallel = Runner.run_sync(focused_parallel_agent, multi_task_question)
    print(result_focused_parallel.final_output)
    
    print("\n💡 Notice:")
    print("• Creative = imaginative responses")
    print("• Conservative = factual and structured")
    print("• Focused Parallel = parallel tools + precise vocabulary")
    print("• Advanced settings work best with OpenAI models")
    
    # 🎯 Summary
    print("\n📊 Model Settings Summary")
    print("-" * 30)
    print("🔹 Gemini (Google):")
    print("  • Temperature control ✅")
    print("  • Tool choice ✅")
    print("  • Sequential tools ✅")
    print("  • Parallel tools ❌")
    print("  • Advanced penalties ❌")
    print()
    print("🔹 OpenAI GPT:")
    print("  • Temperature control ✅")
    print("  • Tool choice ✅")
    print("  • Sequential tools ✅")
    print("  • Parallel tools ✅")
    print("  • Advanced penalties ✅")
    print()
    print("💡 Best Practice: Use Gemini for basic features, OpenAI for advanced features!")


if __name__ == "__main__":
    main()