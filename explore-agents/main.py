import os
from dotenv import load_dotenv


from agents import Agent, Runner, AsyncOpenAI,  OpenAIChatCompletionsModel, RunResult, RunConfig

load_dotenv()

external_client: AsyncOpenAI = AsyncOpenAI(base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
                        api_key = os.getenv("GEMINI_API_KEY"))


llm_model: OpenAIChatCompletionsModel = OpenAIChatCompletionsModel(openai_client= external_client,model = "gemini-2.0-flash")

config: RunConfig = RunConfig(model=llm_model,max_tokens=1000,temperature=0.)

chat_agent: Agent = Agent(name = "chat-agent", model = llm_model, tools = [])

runner: RunResult = Runner.run_sync(starting_agent = chat_agent,input = "What is the capital of France?")

print(runner.final_output)