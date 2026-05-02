from google.adk.agents.llm_agent import Agent
import math

def calculate_rectangle_area(width: float, height: float) -> float:
    """Обчислює площу прямокутника."""
    return width * height

def calculate_circle_area(radius: float) -> float:
    """Обчислює площу кола."""
    return math.pi * radius ** 2

def calculate_cube_volume(side: float) -> float:
    """Обчислює об'єм куба."""
    return side ** 3

# ⭐ ДОДАТКОВИЙ ІНСТРУМЕНТ (для зірочки)
def calculate_triangle_area(base: float, height: float) -> float:
    """
    Обчислює площу трикутника за основою та висотою.
    Args:
        base: основа трикутника
        height: висота трикутника
    Returns:
        float: площа трикутника
    """
    return 0.5 * base * height

# Створюємо математичного агента
root_agent = Agent(
    model='gemini-2.5-flash-lite',
    name='math_agent',
    description="Виконує математичні обчислення геометричних фігур.",
    instruction="""
    Ти експертний математичний асистент який допомагає з обчисленнями.
    У тебе є інструменти для обчислення площі прямокутника, площі кола, об'єму куба та площі трикутника.
    Використовуй ці інструменти коли потрібно виконати розрахунки.
    Відповідай українською мовою та поясни хід обчислень.
    """,
    tools=[
        calculate_rectangle_area, 
        calculate_circle_area, 
        calculate_cube_volume,
        calculate_triangle_area  # Додали новий інструмент сюди
    ],
)