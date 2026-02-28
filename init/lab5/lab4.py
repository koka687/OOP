from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Метод для обчислення площі, який мають реалізувати всі фігури"""
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

# Додаємо новий клас Квадрат
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        # Реалізуємо абстрактний метод: площа квадрата = сторона в квадраті
        return self.side ** 2

# Використання
circle = Circle(5)
square = Square(4)

print(f"Площа кола: {circle.area()}")  # 78.5
print(f"Площа квадрата: {square.area()}") # 16