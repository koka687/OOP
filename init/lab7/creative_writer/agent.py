from google.adk.agents.llm_agent import Agent

def generate_story_prompt(theme: str, characters: int = 2) -> str:
    """Генерує промпт для історії."""
    return f"Створи цікаву історію на тему '{theme}' з {characters} персонажами."

root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='creative_writer',
    description="Креативний письменник історій.",
    instruction="""
    Ти талановитий письменник який створює захоплюючі історії.
    Твої історії мають бути дуже креативними та написаними українською мовою.
    """,
    tools=[generate_story_prompt],
)