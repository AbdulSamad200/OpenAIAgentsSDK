# 🌊 Event Streaming

This project explores the **Streaming capabilities** of the OpenAI Agents SDK. It shows how to track the internal progress of an agent run in real-time, providing visibility into tool calls, agent switches, and intermediate steps.

## ✨ Features

### 📡 Stream Events
- **`Runner.run_streamed`**: Returns an async iterator of events
- **Event Types**: Tracks agent updates, tool calls, and raw token generation

### 🛠️ Interactive Tracing
- **Real-Time Feedback**: Prints status updates to the console as they happen
- **Granular Control**: Filter and process specific event types (e.g., show only tool outputs)

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google Gemini API key

### Installation

1. **Navigate to the directory**
   ```bash
   cd streaming
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the demo**
   ```bash
   uv run main.py
   ```

## 📖 Usage Examples

### Consuming the Stream

```python
result = Runner.run_streamed(agent, input="Tell me a joke")

async for event in result.stream_events():
    if event.type == "run_item_stream_event":
        if event.item.type == "tool_call_item":
            print(f"🛠️ Calling tool: {event.item.function.name}")
        elif event.item.type == "message_output_item":
            print(f"💬 Agent said: {event.item.content}")
```

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/streaming/issues)
- Check the [documentation](https://openai.github.io/openai-agents-python/)
- Contact: kabdulsamad2003@gmail.com

---

**Made with ❤️ for the AI community**