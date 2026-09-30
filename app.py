"""Веб-приложение «Библиотека»: учёт выдачи книг читателям.

Запуск: python app.py
"""
from datetime import date, timedelta

MAX_BOOKS = 5          # не более 5 книг на одного читателя
MAX_DAYS = 30          # срок выдачи не более 30 дней


class Library:
    def __init__(self):
        self.books = {}    # код книги -> название
        self.readers = {}  # код читателя -> фамилия
        self.issues = []   # выдачи: (код книги, код читателя, дата выдачи, дата возврата)

    def add_book(self, book_id, title):
        self.books[book_id] = title

    def add_reader(self, reader_id, surname):
        self.readers[reader_id] = surname

    def books_on_hand(self, reader_id):
        return [i for i in self.issues if i[1] == reader_id and i[3] is None]

    def issue_book(self, book_id, reader_id, day=None):
        if book_id not in self.books:
            raise ValueError("Книга не найдена")
        if reader_id not in self.readers:
            raise ValueError("Читатель не зарегистрирован")
        if len(self.books_on_hand(reader_id)) >= MAX_BOOKS:
            raise ValueError("Нельзя выдать больше 5 книг одному читателю")
        self.issues.append([book_id, reader_id, day or date.today(), None])

    def return_book(self, book_id, reader_id, day=None):
        for issue in self.books_on_hand(reader_id):
            if issue[0] == book_id:
                issue[3] = day or date.today()
                return issue[3] - issue[2] > timedelta(days=MAX_DAYS)  # True = просрочка
        raise ValueError("Эта книга не выдавалась читателю")


if __name__ == "__main__":
    lib = Library()
    lib.add_book(1, "Мастер и Маргарита")
    lib.add_reader(1, "Иванов")
    lib.issue_book(1, 1)
    print("Книг на руках у читателя 1:", len(lib.books_on_hand(1)))
