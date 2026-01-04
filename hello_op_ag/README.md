# 📦 Hello OpenAI Agents (Package)

This is a simple Python package skeleton designed to hold OpenAI Agents SDK examples or reusable components. It follows a standard `src` layout structure, making it a good starting point for building distributable agent libraries.

## 📂 Structure

```
hello_op_ag/
├── src/
│   └── hello_op_ag/
│       └── __init__.py  # Entry point
├── pyproject.toml       # Package configuration
└── README.md
```

## 🚀 Quick Start

### Prerequisites
- Python 3.10+

### Installation

1. **Navigate to the directory**
   ```bash
   cd hello_op_ag
   ```

2. **Install dependencies**
   ```bash
   uv sync
   ```

3. **Run the Package**
   ```bash
   uv run main.py
   ```

## 📖 Usage Examples

### Package Entry Point

```python
# src/hello_op_ag/__init__.py

def main() -> None:
    print("Hello from hello-op-ag!")
    # Initialize your agents here
```

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/hello_op_ag/issues)
- Check the [documentation](https://openai.github.io/openai-agents-python/)
- Contact: kabdulsamad2003@gmail.com

---

**Made with ❤️ for the AI community**