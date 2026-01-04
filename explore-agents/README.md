# 🧭 Explore Agents - Minimal Baseline

This project serves as a minimal, clean baseline for exploring the OpenAI Agents SDK with the Google Gemini model. It strips away complex features to focus on the absolute essentials of defining a model, creating an agent, and executing a single turn.

## ✨ Features

### 🛠️ Essentials Only
- **Model Configuration**: Sets up `OpenAIChatCompletionsModel` with `gemini-2.0-flash`
- **Minimal Agent**: Defines a `chat-agent` with no tools or complex instructions
- **Configuration Control**: Demonstrates how to use `RunConfig` to control parameters

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google Gemini API key

### Installation

1. **Navigate to the directory**
   ```bash
   cd explore-agents
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   Create a `.env` file:
   ```env
   GEMINI_API_KEY=your_key_here
   ```

4. **Run the demo**
   ```bash
   uv run main.py
   ```

## 📖 Usage Examples

### Basic Run

```python
from agents import Agent, Runner, RunConfig

# Setup config
config = RunConfig(
    model=llm_model,
    max_tokens=1000,
    temperature=0.0
)

# Create and run
chat_agent = Agent(name="chat-agent", model=llm_model)
runner = Runner.run_sync(
    starting_agent=chat_agent,
    input="What is the capital of France?"
)
print(runner.final_output)
```

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/explore-agents/issues)
- Check the [documentation](https://openai.github.io/openai-agents-python/)
- Contact: kabdulsamad2003@gmail.com

---

**Made with ❤️ for the AI community**