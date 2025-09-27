# 🤖 Hello Agent - Multi-Agent AI System

A sophisticated demonstration of multi-agent AI systems using the OpenAI Agents SDK. This project showcases how specialized AI agents can work together to solve complex problems across different domains including education, business, and technical tasks.

## ✨ Features

### 🎯 Multi-Agent Architecture
- **Specialized Agents**: Each agent is designed for specific domains (education, business, technical)
- **Intelligent Routing**: Coordinator agents automatically route tasks to appropriate specialists
- **Collaborative Problem Solving**: Multiple agents can work together on complex problems

### 🎓 Educational Agents
- **Mathematics Tutor**: Expert in algebra, calculus, statistics, and problem-solving
- **History Tutor**: Specialized in historical analysis and context
- **Science Tutor**: Covers physics, chemistry, biology, and scientific methods
- **Literature Tutor**: Focuses on literary analysis and creative writing

### 💼 Professional Agents
- **Business Analyst**: Market research, strategy, and financial analysis
- **Software Architect**: System design, scalability, and best practices
- **Data Scientist**: Statistical analysis, machine learning, and data visualization
- **Project Manager**: Planning, risk management, and team coordination

### 🔬 Research & Technical Agents
- **Research Specialist**: Information gathering and fact-checking
- **Technical Specialist**: Programming, debugging, and technology solutions
- **Creative Director**: Innovation, brainstorming, and design thinking

## 🚀 Quick Start

### Prerequisites
- Python 3.11 or higher
- Google Gemini API key

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/hello-agent.git
   cd hello-agent
   ```

2. **Install dependencies**
   ```bash
   pip install -e .
   ```

3. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env and add your GEMINI_API_KEY
   ```

4. **Run the demo**
   ```bash
   python main.py
   ```

## 📖 Usage Examples

### Basic Usage

```python
from agents import Agent, Runner

# Create a specialized agent
math_tutor = Agent(
    name="Math Tutor",
    instructions="You are an expert mathematics tutor..."
)

# Run the agent
result = await Runner.run(math_tutor, "Solve this equation: 2x + 5 = 13")
print(result.final_output)
```

### Multi-Agent Coordination

```python
from agent import create_coordinator_agents

# Get coordinator agents
educational_coordinator, professional_coordinator = create_coordinator_agents()

# The coordinator will automatically route to appropriate specialists
result = await Runner.run(educational_coordinator, "Explain quantum physics")
```

### Interactive Mode

The application includes an interactive mode where you can ask questions directly:

```bash
python main.py
# Follow the prompts to try interactive mode
```

## 🏗️ Project Structure

```
hello_agent/
├── main.py              # Main application with demo scenarios
├── agent.py             # Pre-configured specialized agents
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
├── .env.example         # Environment variables template
└── .gitignore           # Git ignore rules
```

## 🎮 Demo Scenarios

The application includes several demo scenarios that showcase different agent capabilities:

1. **📊 Mathematical Problem Solving** - Complex equation solving with step-by-step explanations
2. **🔬 Research and Analysis** - Comprehensive research on AI in education
3. **💡 Creative Brainstorming** - Innovative ideas for sustainable smart cities
4. **💻 Technical Solutions** - Microservices architecture design
5. **🎯 Multi-Domain Tasks** - Complex projects requiring multiple specialists

## 🔧 Configuration

### Environment Variables

Create a `.env` file with the following variables:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

### Agent Customization

You can easily create custom agents by extending the base `Agent` class:

```python
custom_agent = Agent(
    name="Custom Specialist",
    instructions="Your custom instructions here...",
    handoff_description="Description for task routing"
)
```

## 🧪 Development

### Running Tests

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest
```

### Code Quality

```bash
# Format code
black .

# Lint code
flake8 .

# Type checking
mypy .
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [OpenAI Agents SDK](https://github.com/openai/agents) for the powerful agent framework
- [Google Gemini](https://ai.google.dev/) for the language model capabilities
- The AI community for inspiration and collaboration

## 📞 Support

If you have any questions or need help:

- Open an [issue](https://github.com/AbdulSamad200/hello-agent/issues)
- Check the [documentation](https://github.com/AbdulSamad200/hello-agent/wiki)
- Contact: your.email@example.com

---

**Made with ❤️ for the AI community**

