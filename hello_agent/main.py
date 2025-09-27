"""
Hello Agent - A Multi-Agent AI System Demo
==========================================

This project demonstrates a sophisticated multi-agent system using OpenAI Agents SDK.
It showcases different specialized agents working together to solve complex problems.
"""

import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, AsyncOpenAI, OpenAIChatCompletionsModel, Runner

# Load environment variables
load_dotenv()

# Configuration
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("❌ Error: GEMINI_API_KEY not found in environment variables.")
    print("Please create a .env file with your GEMINI_API_KEY")
    exit(1)

# Initialize OpenAI client for Gemini
external_client = AsyncOpenAI(
    api_key=GEMINI_API_KEY, 
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Configure the language model
llm_model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=external_client,
)

# Define specialized agents
def create_agents():
    """Create and configure specialized agents for different tasks."""
    
    # Research Agent - Specialized in gathering and analyzing information
    research_agent = Agent(
        name="Research Specialist",
        instructions="""
        You are a research specialist with expertise in:
        - Gathering and analyzing information from various sources
        - Fact-checking and verifying information
        - Providing comprehensive overviews of complex topics
        - Breaking down complex subjects into understandable components
        
        Always provide well-researched, accurate information with proper context.
        """,
        handoff_description="Expert researcher for information gathering and analysis"
    )
    
    # Math Agent - Specialized in mathematical problems and calculations
    math_agent = Agent(
        name="Mathematics Expert",
        instructions="""
        You are a mathematics expert specializing in:
        - Solving complex mathematical problems
        - Explaining mathematical concepts clearly
        - Providing step-by-step solutions
        - Working with various mathematical fields (algebra, calculus, statistics, etc.)
        
        Always show your work and explain your reasoning step by step.
        """,
        handoff_description="Mathematics expert for calculations and problem-solving"
    )
    
    # Creative Agent - Specialized in creative tasks and brainstorming
    creative_agent = Agent(
        name="Creative Director",
        instructions="""
        You are a creative director with expertise in:
        - Creative writing and storytelling
        - Brainstorming and ideation
        - Design thinking and innovation
        - Artistic and creative problem-solving
        
        Always think outside the box and provide innovative, creative solutions.
        """,
        handoff_description="Creative expert for artistic and innovative tasks"
    )
    
    # Technical Agent - Specialized in programming and technical solutions
    technical_agent = Agent(
        name="Technical Specialist",
        instructions="""
        You are a technical specialist with expertise in:
        - Programming and software development
        - Technical architecture and design
        - Debugging and problem-solving
        - Technology trends and best practices
        
        Always provide practical, implementable technical solutions.
        """,
        handoff_description="Technical expert for programming and engineering tasks"
    )
    
    # Coordinator Agent - Routes tasks to appropriate specialists
    coordinator_agent = Agent(
        name="Task Coordinator",
        instructions="""
        You are a task coordinator responsible for:
        - Analyzing user requests and determining the best approach
        - Routing tasks to appropriate specialist agents
        - Coordinating multi-step processes
        - Ensuring comprehensive solutions
        
        Based on the user's request, determine which specialist agent(s) should handle the task.
        For complex tasks, you may need to coordinate multiple agents.
        """,
        handoffs=[research_agent, math_agent, creative_agent, technical_agent]
    )
    
    return coordinator_agent, research_agent, math_agent, creative_agent, technical_agent

async def run_demo_scenarios():
    """Run various demo scenarios to showcase the multi-agent system."""
    
    coordinator, research, math, creative, technical = create_agents()
    
    print("🤖 Hello Agent - Multi-Agent AI System Demo")
    print("=" * 50)
    
    # Demo scenarios
    scenarios = [
        {
            "title": "📊 Mathematical Problem Solving",
            "query": "Solve this complex equation: 2x³ - 5x² + 3x - 1 = 0. Show all steps and explain the solution method.",
            "expected_agent": "Mathematics Expert"
        },
        {
            "title": "🔬 Research and Analysis",
            "query": "Research the impact of artificial intelligence on modern education. Provide a comprehensive analysis with key findings and trends.",
            "expected_agent": "Research Specialist"
        },
        {
            "title": "💡 Creative Brainstorming",
            "query": "Help me brainstorm innovative ideas for a sustainable smart city project. Think creatively about technology, environment, and community.",
            "expected_agent": "Creative Director"
        },
        {
            "title": "💻 Technical Solution",
            "query": "Design a scalable microservices architecture for an e-commerce platform. Include database design, API structure, and deployment strategy.",
            "expected_agent": "Technical Specialist"
        },
        {
            "title": "🎯 Complex Multi-Domain Task",
            "query": "I want to create an educational app that teaches mathematics through gamification. Help me plan the technical implementation, educational content strategy, and user engagement features.",
            "expected_agent": "Task Coordinator (will route to multiple specialists)"
        }
    ]
    
    for i, scenario in enumerate(scenarios, 1):
        print(f"\n{i}. {scenario['title']}")
        print(f"Query: {scenario['query']}")
        print(f"Expected Agent: {scenario['expected_agent']}")
        print("-" * 50)
        
        try:
            result = await Runner.run(coordinator, scenario['query'])
            print(f"🤖 Agent Response:\n{result.final_output}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("\n" + "="*50)

async def interactive_mode():
    """Run the system in interactive mode for user queries."""
    coordinator, _, _, _, _ = create_agents()
    
    print("\n🎮 Interactive Mode")
    print("Ask me anything! Type 'quit' to exit.")
    print("-" * 30)
    
    while True:
        try:
            user_input = input("\n💬 Your question: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("👋 Goodbye!")
                break
                
            if not user_input:
                continue
                
            print("🤖 Processing...")
            result = await Runner.run(coordinator, user_input)
            print(f"\n🤖 Response:\n{result.final_output}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {str(e)}")

async def main():
    """Main function to run the demo."""
    print("🚀 Starting Hello Agent Demo...")
    
    # Run demo scenarios
    await run_demo_scenarios()
    
    # Ask if user wants to try interactive mode
    print("\n" + "="*50)
    try:
        choice = input("Would you like to try interactive mode? (y/n): ").strip().lower()
        if choice in ['y', 'yes']:
            await interactive_mode()
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")

if __name__ == "__main__":
    asyncio.run(main())