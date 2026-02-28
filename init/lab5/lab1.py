import random

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner  # публічний атрибут
        self.__balance = balance  # приватний атрибут (інкапсуляція)

    def deposit(self, amount):
        self.__balance += amount
        print(f"Поповнення: +{amount} грн")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            print(f"Зняття: -{amount} грн")
            return amount
        else:
            print(f"Спроба зняти {amount} грн: Недостатньо коштів!")
            return "Insufficient funds"

    def get_balance(self):
        return self.__balance

# Створюємо об'єкт
account = BankAccount("Bohdan", 1000)
print(f"Початковий баланс: {account.get_balance()} грн\n")

# Цикл для виконання 5 випадкових операцій
for i in range(5):
    action = random.choice(['deposit', 'withdraw'])
    amount = random.randint(100, 500) # випадкова сума від 100 до 500
    
    if action == 'deposit':
        account.deposit(amount)
    else:
        account.withdraw(amount)

# Виведення кінцевого результату
print(f"\nКінцевий баланс: {account.get_balance()} грн")