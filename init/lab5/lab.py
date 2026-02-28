from abc import ABC, abstractmethod
from random import randint, choice

# 1. АБСТРАКЦІЯ
class Item(ABC):
    def __init__(self, name: str, health=500):
        self.name = name
        self.health = health
    
    @abstractmethod
    def attack(self, another_item):
        pass

    @abstractmethod
    def buff(self):
        """Метод для підсилення зброї (заточування, прицілювання тощо)"""
        pass

# 2. НАСЛІДУВАННЯ ТА ПОЛІМОРФІЗМ
class Sword(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        # 3. ІНКАПСУЛЯЦІЯ
        self.__attack_power = attack_power 
        self._sharp = 0
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + self._sharp + randint(0, 10)
        another_item.health -= current_attack
        return f"⚔️ {self.name} січе на {current_attack} шкоди! У {another_item.name} HP: {max(0, another_item.health)}"
    
    def buff(self):
        self._sharp += 5
        return f"✨ {self.name} заточено! Поточна гострота: +{self._sharp}"

class Axe(Item):
    def __init__(self, name, attack_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(0, 25) # Вищий розкид шкоди
        another_item.health -= current_attack
        return f"🪓 {self.name} врубується на {current_attack} шкоди! У {another_item.name} HP: {max(0, another_item.health)}"

    def buff(self):
        # Сокира просто лютує, додаючи до базової атаки
        self.__attack_power += 2
        return f"🔥 {self.name} стає важчою! Базова атака зросла."

# НОВИЙ ТИП ЗБРОЇ - ЛУК
class Bow(Item):
    def __init__(self, name, attack_power: int, range_power: int):
        super().__init__(name=name)
        self.__attack_power = attack_power
        self.range_power = range_power # Специфічний параметр для лука
    
    def attack(self, another_item: Item):
        current_attack = self.__attack_power + randint(5, 15) + self.range_power
        another_item.health -= current_attack
        return f"🏹 {self.name} випускає стрілу на {current_attack} шкоди! У {another_item.name} HP: {max(0, another_item.health)}"

    def buff(self):
        self.range_power += 1
        return f"🎯 {self.name} перезаряджено. Дальність прицілювання зросла до {self.range_power}!"

# --- ЛОГІКА ГРИ ---

# Списки для випадкового вибору
weapon_types = [
    lambda: Sword("Ескалібур", 40),
    lambda: Axe("Гнів Кратоса", 35),
    lambda: Bow("Око Сокола", 30, 10)
]

player = weapon_types[randint(0, 2)]()
enemy = weapon_types[randint(0, 2)]()

print(f"🎮 ГРА ПОЧАЛАСЯ! Ви отримали: {type(player).__name__} ({player.name})")
print(f"👾 Ваш ворог: {type(enemy).__name__} ({enemy.name})\n")

round_num = 1
while player.health > 0 and enemy.health > 0:
    print(f"--- Хід {round_num} ---")
    print(f"Ваше HP: {player.health} | HP Ворога: {enemy.health}")
    
    # Хід гравця
    choice_action = input("Виберіть дію: 1 - Атака, 2 - Підсилення (buff): ")
    if choice_action == "1":
        print(player.attack(enemy))
    else:
        print(player.buff())
    
    if enemy.health <= 0:
        print(f"\n🏆 ПЕРЕМОГА! {enemy.name} подолано.")
        break
    
    # Хід комп'ютера (випадковий)
    enemy_action = randint(1, 2)
    if enemy_action == 1:
        print(enemy.attack(player))
    else:
        print(f"👾 Ворог готується... {enemy.buff()}")

    if player.health <= 0:
        print(f"\n💀 ВИ ПРОГРАЛИ! {player.name} зламано.")
        break
    
    round_num += 1
    print("-" * 20)