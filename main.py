import os
from dotenv import load_dotenv
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from travel_tool import get_fligthts,get_hotels

# Load environment variables from .env file
load_dotenv()
# Initialize the OpenAI model

client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # Adjust the base URL as needed
)

model = OpenAIChatCompletionsModel(model="gemini-2.0-flash",openai_client=client)
config = RunConfig(model=model, tracing_disabled=True)

# Create an agent with the model and tools
destination_agent = Agent(
    name="DestinationAgent",
    instructions="You are a travel agent. You recommend destination according to wish.",
    model=model,
)

booking_agent = Agent(
    name="BookingAgent",
    instructions="You are a booking agent. You can book flights and hotels information using tools.",
    model=model,
    tools=[get_fligthts, get_hotels],
)

explore_agent = Agent(
    name="ExploreAgent",
    instructions="You are an exploration agent. You can provide information about destinations like about food and different famous place.",
    model=model,
)

def main():
    print("🌍Welcome to the Travel Agent!")
    wish = input("What is your wish? (e.g., I wish, I will go to picnic at the waves & saw sunset & feel scent of water waves & Breathe cool air (karachi) ) ->")

    result1 = Runner.run_sync(destination_agent, wish, run_config=config)
    dest = result1.final_output.strip()
    print(f"✈️Destination suggested: {dest}")


    result2 = Runner.run_sync(booking_agent, dest, run_config=config)
    print(f"Booking information: {result2.final_output}")

    result3 = Runner.run_sync(explore_agent, dest, run_config=config)
    print(f"Exploration information: {result3.final_output}")

    print("Thank you for using the Travel Agent! Have a great trip!")

if __name__ == "__main__":
    main()    