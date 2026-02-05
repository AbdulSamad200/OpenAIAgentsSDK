# 🔗 Chainlit Hello World

This project demonstrates how to build a **Chat UI** for your AI agents using [Chainlit](https://docs.chainlit.io/). It bridges the gap between the headless OpenAI Agents SDK and a user-friendly web interface.

## ✨ Features

### 💬 Interactive UI
- **Chat Interface**: Clean, modern web UI for messaging your agent
- **History Management**: Maintains conversation context across multiple turns
- **Async Integration**: Fully asynchronous event loop handling for responsive UI

### 🏗️ Architecture
- **Session State**: Stores conversation history in the user session
- **Event-Driven**: Uses `@cl.on_message` to react to user input

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google Gemini API key

### Installation

1. **Navigate to the directory**
   ```bash
   cd chainlit_hello
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

4. **Launch the UI**
   ```bash
   uv run chainlit run hello.py -w
   ```

## 📖 Usage Examples

### Connecting Agent to Chainlit

```python
import chainlit as cl
from agents import Runner

@cl.on_message
async def handle_message(message: cl.Message):
    # Retrieve history
    history = cl.user_session.get("history")
    history.append({"role":"user", "content":message.content})

    # Run Agent
    result = await Runner.run(
        agent,
        input=history,
        run_config=run_config
    )
    
    # Send response
    await cl.Message(content=result.final_output).send()
```

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/chainlit_hello/issues)
- Check the [documentation](https://openai.github.io/openai-agents-python/)
- Contact: kabdulsamad2003@gmail.com

---

**Made with ❤️ for the AI community**