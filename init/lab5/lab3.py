class Animal:
    def speak(self):
        # Батьківський метод нічого не робить
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

# Створюємо клас Fish без власного методу speak
class Fish(Animal):
    pass

# Перевірка
animals = [Dog(), Cat(), Fish()]

for animal in animals:
    print(f"{type(animal).__name__} каже: {animal.speak()}")