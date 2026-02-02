# 🛠️ Hello Tools

This project demonstrates how to create, test, and use custom tools with the **OpenAI Agents SDK**. It features a collection of practical tools (Calculator, Weather, Web Search, Text Summarizer) and shows how to bundle them into an agent.

## ✨ Features

### 🧰 Custom Tool Suite
- **`calculator`**: Performs safe mathematical evaluations on string expressions
- **`text_summarizer`**: Condenses long text inputs into shorter summaries
- **`weather_fetcher`**: Provides mock weather data for demonstration purposes
- **`web_search`**: Integrates with the **Tavily API** for real-time web information

### 🎮 Modes
- **Interactive Mode**: Chat interface where the agent dynamically selects tools
- **Standalone Demos**: Scripts to test tools individually (`examples.py`)

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google Gemini API key
- Tavily API key (optional)

### Installation

1. **Navigate to the directory**
   ```bash
   cd hello_tools
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   Create a `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_key
   TAVILY_API_KEY=your_tavily_key
   ```

4. **Run the agent**
   ```bash
   uv run main.py
   ```

## 📖 Usage Examples

### Defining a Tool

```python
from agents import function_tool

@function_tool
def calculator(expression: str) -> str:
    """
    Perform basic mathematical calculations.
    Args:
        expression: A math expression (e.g., "5 + 5")
    """
    try:
        return f"Result: {eval(expression)}"
    except Exception as e:
        return f"Error: {str(e)}"

# Add to agent
agent = Agent(
    name="MathBot",
    tools=[calculator],
    model=llm_model
)
```

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/hello_tools/issues)
- Check the [documentation](https://openai.github.io/openai-agents-python/)
- Contact: kabdulsamad2003@gmail.com

---

**Made with ❤️ for the AI community**
