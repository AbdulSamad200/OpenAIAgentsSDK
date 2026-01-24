# ⚙️ Hello Model Settings

This project provides a comprehensive guide to configuring **Model Settings** in the OpenAI Agents SDK. It demonstrates how to fine-tune the behavior of both **Google Gemini** and **OpenAI GPT** models, covering parameters like temperature, tool choice, and advanced penalties.

## ✨ Features

### 🌡️ Temperature Control
- **Cold Agent (0.1)**: Deterministic, focused, and factual
- **Hot Agent (1.9)**: Creative, random, and diverse

### 🛠️ Tool Choice Strategies
- **`auto`**: The model decides whether to use a tool
- **`required`**: Forces the model to use a tool
- **`none`**: Prevents the model from using any tools

### ⚡ Execution Modes
- **Sequential Tool Calls**: Demonstrated with Gemini (tools run one after another)
- **Parallel Tool Calls**: Demonstrated with OpenAI (multiple tools run simultaneously)

### 🎛️ Advanced Parameters (OpenAI only)
- **`top_p`**: Controls vocabulary diversity
- **`frequency_penalty`**: Reduces repetition of words
- **`presence_penalty`**: Encourages introducing new topics

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google Gemini API key
- OpenAI API key (optional)

### Installation

1. **Navigate to the directory**
   ```bash
   cd hello_settings
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Set up environment variables**
   Create a `.env` file:
   ```env
   GEMINI_API_KEY=your_gemini_key
   OPENAI_API_KEY=your_openai_key
   ```

4. **Run the demo**
   ```bash
   uv run main.py
   ```

## 📖 Usage Examples

### Configuring Model Settings

```python
from agents import Agent, ModelSettings

# High creativity agent
creative_agent = Agent(
    name="Creative",
    model=model,
    model_settings=ModelSettings(
        temperature=1.5,
        top_p=0.9,
        frequency_penalty=0.8
    )
)

# Focused agent forcing a tool
focused_agent = Agent(
    name="Focused",
    model=model,
    tools=[my_tool],
    model_settings=ModelSettings(
        tool_choice="required",
        temperature=0.1
    )
)
```

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/hello_settings/issues)
- Check the [documentation](https://openai.github.io/openai-agents-python/)
- Contact: kabdulsamad2003@gmail.com

---

**Made with ❤️ for the AI community**