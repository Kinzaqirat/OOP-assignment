class Book:
    total_books = 0 \

    def __init__(self, title):
        self.title = title
        Book.increment_book_count() 
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1


book1 = Book("Python 101")
book2 = Book("OOP in Python")
book3 = Book("AI for Beginners")


print("Total books added:", Book.total_books)
