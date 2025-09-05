from agents import function_tool

@function_tool
def get_fligthts( destination: str) -> str:
    return f"Flights found to {destination} : PKR 45,000 - PKR 70,000."

@function_tool
def get_hotels(destination: str) -> str:
    return f"hotels in {destination} : Avari hotel, Pearl Continental, Serena hotel."