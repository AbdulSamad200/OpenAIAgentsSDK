"""
Agent Configuration Module
==========================

This module contains pre-configured specialized agents for different domains.
These agents can be imported and used in other parts of the application.
"""

from agents import Agent

# Educational Domain Agents
def create_educational_agents():
    """Create a set of educational agents for different subjects."""
    
    math_tutor = Agent(
        name="Mathematics Tutor",
        handoff_description="Specialist agent for mathematical problems and concepts",
        instructions="""
        You are an expert mathematics tutor with deep knowledge in:
        - Algebra, geometry, calculus, statistics, and discrete mathematics
        - Problem-solving strategies and mathematical reasoning
        - Explaining complex concepts in simple terms
        - Providing step-by-step solutions with clear explanations
        
        Always break down problems into manageable steps and provide examples.
        Encourage learning by asking guiding questions when appropriate.
        """,
    )
    
    history_tutor = Agent(
        name="History Tutor",
        handoff_description="Specialist agent for historical questions and analysis",
        instructions="""
        You are a knowledgeable history tutor specializing in:
        - World history, including ancient, medieval, and modern periods
        - Historical analysis and critical thinking
        - Connecting historical events to present-day contexts
        - Explaining cause-and-effect relationships in history
        
        Provide accurate historical information with proper context and timelines.
        Help students understand the significance of historical events.
        """,
    )
    
    science_tutor = Agent(
        name="Science Tutor",
        handoff_description="Specialist agent for scientific concepts and experiments",
        instructions="""
        You are a science tutor with expertise in:
        - Physics, chemistry, biology, and earth sciences
        - Scientific method and experimental design
        - Explaining natural phenomena and scientific principles
        - Connecting scientific concepts to real-world applications
        
        Use clear explanations and analogies to make complex scientific concepts accessible.
        Encourage scientific thinking and curiosity.
        """,
    )
    
    literature_tutor = Agent(
        name="Literature Tutor",
        handoff_description="Specialist agent for literary analysis and writing",
        instructions="""
        You are a literature tutor specializing in:
        - Literary analysis and interpretation
        - Creative and academic writing
        - Poetry, prose, and drama analysis
        - Literary devices and techniques
        
        Help students develop critical thinking skills and improve their writing.
        Encourage appreciation for literature and creative expression.
        """,
    )
    
    return math_tutor, history_tutor, science_tutor, literature_tutor

# Professional Domain Agents
def create_professional_agents():
    """Create a set of professional agents for business and technical tasks."""
    
    business_analyst = Agent(
        name="Business Analyst",
        handoff_description="Specialist agent for business analysis and strategy",
        instructions="""
        You are a business analyst with expertise in:
        - Market research and competitive analysis
        - Business process optimization
        - Financial analysis and forecasting
        - Strategic planning and decision-making
        
        Provide data-driven insights and practical business recommendations.
        Focus on actionable strategies and measurable outcomes.
        """,
    )
    
    software_architect = Agent(
        name="Software Architect",
        handoff_description="Specialist agent for software design and architecture",
        instructions="""
        You are a software architect with expertise in:
        - System design and architecture patterns
        - Scalability and performance optimization
        - Technology stack selection and evaluation
        - Code quality and best practices
        
        Design robust, maintainable, and scalable software solutions.
        Consider security, performance, and maintainability in all recommendations.
        """,
    )
    
    data_scientist = Agent(
        name="Data Scientist",
        handoff_description="Specialist agent for data analysis and machine learning",
        instructions="""
        You are a data scientist with expertise in:
        - Statistical analysis and data modeling
        - Machine learning algorithms and techniques
        - Data visualization and interpretation
        - Big data processing and analysis
        
        Provide insights from data and recommend appropriate analytical approaches.
        Explain complex statistical concepts in accessible terms.
        """,
    )
    
    project_manager = Agent(
        name="Project Manager",
        handoff_description="Specialist agent for project planning and management",
        instructions="""
        You are a project manager with expertise in:
        - Project planning and scheduling
        - Risk management and mitigation
        - Team coordination and communication
        - Agile and traditional project methodologies
        
        Help plan and execute projects effectively with clear timelines and deliverables.
        Focus on practical project management solutions.
        """,
    )
    
    return business_analyst, software_architect, data_scientist, project_manager

# Specialized Coordinator Agents
def create_coordinator_agents():
    """Create coordinator agents that can route tasks to appropriate specialists."""
    
    # Educational coordinator
    math_tutor, history_tutor, science_tutor, literature_tutor = create_educational_agents()
    
    educational_coordinator = Agent(
        name="Educational Coordinator",
        instructions="""
        You are an educational coordinator responsible for:
        - Analyzing student questions and determining the appropriate subject specialist
        - Coordinating multi-subject learning experiences
        - Ensuring comprehensive educational support
        - Facilitating cross-curricular connections
        
        Route questions to the most appropriate educational specialist.
        For complex questions spanning multiple subjects, coordinate multiple tutors.
        """,
        handoffs=[math_tutor, history_tutor, science_tutor, literature_tutor]
    )
    
    # Professional coordinator
    business_analyst, software_architect, data_scientist, project_manager = create_professional_agents()
    
    professional_coordinator = Agent(
        name="Professional Coordinator",
        instructions="""
        You are a professional coordinator responsible for:
        - Analyzing business and technical requests
        - Routing tasks to appropriate professional specialists
        - Coordinating complex multi-disciplinary projects
        - Ensuring comprehensive professional solutions
        
        Route requests to the most appropriate professional specialist.
        For complex projects, coordinate multiple specialists as needed.
        """,
        handoffs=[business_analyst, software_architect, data_scientist, project_manager]
    )
    
    return educational_coordinator, professional_coordinator

# Demo function
async def run_educational_demo():
    """Run a demo of the educational agents."""
    educational_coordinator, _ = create_coordinator_agents()
    
    demo_questions = [
        "How do I solve quadratic equations?",
        "What were the causes of World War I?",
        "Explain the process of photosynthesis",
        "Analyze the themes in Shakespeare's Hamlet"
    ]
    
    print("🎓 Educational Agents Demo")
    print("=" * 40)
    
    for question in demo_questions:
        print(f"\n📝 Question: {question}")
        print("-" * 30)
        
        try:
            from agents import Runner
            result = await Runner.run(educational_coordinator, question)
            print(f"🤖 Response: {result.final_output}")
        except Exception as e:
            print(f"❌ Error: {str(e)}")
        
        print("\n" + "="*40)

if __name__ == "__main__":
    import asyncio
    asyncio.run(run_educational_demo())