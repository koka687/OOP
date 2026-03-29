import os

# Спробуємо дістати значення нашої змінної
print(f"Значення змінної IT_TEST = {os.environ.get('IT_TEST', 'Змінна не знайдена')}")
