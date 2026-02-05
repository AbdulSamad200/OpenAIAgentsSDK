import chainlit as cl
from agents import Agent, RunConfig, AsyncOpenAI, OpenAIChatCompletionsModel,  Runner
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")


# Step 1 : Provider
provider = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Step 2 : Model
model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash-exp",
    openai_client=provider,
)

# Config: Defined at Run Level
run_config = RunConfig(
    model = model,
    model_provider = provider,
    tracing_disabled = True
)


# Step 3 : Agent

agent = Agent(
    instructions = "You are a helpful assistant that can answer questions and help with tasks",
    name = "Panversity Support Agent",
)


# Step 4 : Run

result = Runner.run_sync(
    input = "What is the capital of France",
    run_config = run_config,
    starting_agent = agent
)

@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history",[])
    await cl.Message(content = "Helllo! I am Paneversity Support Agent. How can I help u today?").send()


@cl.on_message
async def handle_message(message: cl.Message):

    history = cl.user_session.get("history")

    history.append({"role":"user","content":message.content})

    result = await Runner.run(
        agent,
        input = history,
        run_config = run_config
    )
    history.append({"role":"user","content":result.final_output})
    cl.user_session.set("history",history)
    await cl.Message(content=result.final_output).send()





