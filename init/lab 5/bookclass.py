from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from studentclass import Student

class BookState(Enum):
    AVAILABLE = "Доступна"
    BORROWED = "Позичена"
    RESERVED = "Зарезервована"
    LOST = "Втрачена"

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
        self.state = BookState.AVAILABLE
        self.borrower: "Student" = None  # Студент, який позичив книгу

    @property
    def description(self):
        return f"Назва: '{self.title}',\n Автор: {self.author},\n Опубліковано в {self.year_published}."
    
    def set_who_borrowed(self, student: "Student"):
        self.state = BookState.BORROWED
        self.borrower = student
    
    def set_release_borrower(self):
        self.state = BookState.AVAILABLE
        self.borrower = None
    
    def __str__(self):
        return f"Книга: '{self.title}'"
    
if __name__ == "__main__":
    # Приклад використання
    book = Book(title="Програмування на Python", author="Автор Не вказано", year_published=2025)
    print(book)
    print(book.description)
    print(f"Стан книги: {book.state.value}")
    333