class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        return f"{self.brand} {self.model}"

    # Додаємо новий метод у базовий клас
    def start_engine(self):
        return f"Двигун автомобіля {self.brand} заведено. Поїхали!"

class Car(Vehicle):
    def __init__(self, brand, model, seats):
        super().__init__(brand, model)
        self.seats = seats

    def display_info(self):
        # Використовуємо super() для розширення логіки батьківського методу
        return f"{super().display_info()}, Кількість місць: {self.seats}"

# Створюємо об'єкт класу Car
my_car = Car("Toyota", "Camry", 5)

# 1. Викликаємо метод, який є в самому класі Car
print(f"Інфо: {my_car.display_info()}")

# 2. Викликаємо НОВИЙ метод, який ми створили в Vehicle, через об'єкт Car
# Це працює завдяки наслідуванню!
print(my_car.start_engine())