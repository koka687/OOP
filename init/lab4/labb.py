class MyName:
    total_names = 0 #Class Variable

    def __init__(self, name=None) -> None:
        if name is not None:
            if not name.replace(" ", "").isalpha():
                raise ValueError("Ім'я може містити лише літери!")
            name = name.capitalize()
        self.name = name if name is not None else self.anonymous_user().name #Class attributes / Instance variables
        MyName.total_names += 1 #modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str: 
        return f"My name is {self.name}"
    
    @property
    def my_email(self) -> str:
        return self.create_email()
    
    @property
    def full_name(self) -> str:
        return f"User #{self.my_id}: {self.name} ({self.my_email})"
    
    def create_email(self, domain="itcollege.lviv.ua") -> str:
        return f"{self.name.lower()}@{domain}"

    def count_letters(self) -> int:
        return len(self.name.replace(" ", ""))
    
    def save_to_file(self, filename="users.txt") -> None:
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"{self.full_name}\n")

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")
    
    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", "Anna", None)
all_names = {}

for name in names:
    try:
        all_names[name] = MyName(name)
    except ValueError as e:
        print(f"Помилка при створенні {name}: {e}")
        all_names[name] = MyName("InvalidName")

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call: {me.create_email()}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
{"<*>"*20}""")

    me.save_to_file()

print(f"We are done. We create {MyName.total_names} names! ??? Why {MyName.total_names}?")

print(f"Створено {MyName.total_names} імен!")

print("\n" + "="*50)
user = MyName("Test")
print(f"Звичайний email: {user.create_email()}")
print(f"Кастомний email: {user.create_email('gmail.com')}")

print("\n" + "="*50)
try:
    bad_user = MyName("User123")
except ValueError as e:
    print(f"Помилка: {e}")