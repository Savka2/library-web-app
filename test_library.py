"""Модульные тесты для app.py (запуск: pytest test_library.py)."""
import pytest
from app import Library, MAX_BOOKS


@pytest.fixture
def lib():
    lib = Library()
    for i in range(1, 8):
        lib.add_book(i, f"Книга {i}")
    lib.add_reader(1, "Иванов")
    return lib


def test_issue_book(lib):
    lib.issue_book(1, 1)
    assert len(lib.books_on_hand(1)) == 1


def test_limit_five_books(lib):
    for book_id in range(1, MAX_BOOKS + 1):
        lib.issue_book(book_id, 1)
    with pytest.raises(ValueError):
        lib.issue_book(6, 1)  # граничное значение: шестая книга


def test_unknown_reader(lib):
    with pytest.raises(ValueError):
        lib.issue_book(1, 99)


def test_return_book(lib):
    lib.issue_book(2, 1)
    lib.return_book(2, 1)
    assert lib.books_on_hand(1) == []
