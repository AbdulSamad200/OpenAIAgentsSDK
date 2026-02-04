# 🏗️ Structured Outputs (st)

This project demonstrates how to enforce **Structured Outputs** in the OpenAI Agents SDK using **Pydantic models**. This is a critical feature for building production applications where the AI's response must be reliably parsed by code.

## ✨ Features

### 📋 Pydantic Integration
- **Schema Definition**: Uses standard `BaseModel` to define the expected response format
- **`output_type`**: Configures the agent to return JSON matching the schema

### 🎯 Type-Safe Results
- **Automatic Parsing**: The SDK converts the raw JSON into a validated Pydantic object
- **Field Access**: Access data using dot notation with full IDE support

## 🚀 Quick Start

### Prerequisites
- Python 3.10+
- Google Gemini API key

### Installation

1. **Navigate to the directory**
   ```bash
   cd st
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

### Defining and Using Output Models

```python
from pydantic import BaseModel
from agents import Agent

class PersonInfo(BaseModel):
    name: str
    age: int
    occupation: str

# Create agent with structured output
agent = Agent(
    name="Extractor",
    model=llm_model,
    output_type=PersonInfo
)

# Run and access fields directly
result = await Runner.run(agent, "I'm Alice, 25, teacher.")
print(f"Name: {result.final_output.name}")  # "Alice"
```

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/st/issues)
- Check the [documentation](https://openai.github.io/openai-agents-python/)
- Contact: kabdulsamad2003@gmail.com

---

**Made with ❤️ for the AI community**