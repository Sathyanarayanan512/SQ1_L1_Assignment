class Book:
    def __init__(self, title, author):
        self.title=title
        self.author=author
        self.status=True
    def __str__(self):
        return f"{self.title} by {self.author} [{'Available' if self.status else 'Not Available'}]"
class Library:
    def __init__(self):
        self.books=[]
    def add_book(self, title, author):
        book=Book(title, author)
        self.books.append(book)
    def borrow_book(self, title):
        for i in self.books:
            if i.title==title:
                if i.status:
                    i.status=False
                else:
                    print(f"Sorry, '{title}' is already borrowed")
                return
        print(f"No book titled '{title}'")
    def return_book(self, title):
        for i in self.books:
            if i.title==title:
                if not i.status:
                    i.status=True
                else:
                    print(f"'{title}' was not borrowed")
                return
    def show_books(self):
        for i in self.books:
            print(i)
        print()
library=Library()
library.add_book('Python 101', 'Sathya')
library.show_books()
library.add_book('Java 101', 'Narayanan')
library.show_books()
library.borrow_book('Python 101')
library.show_books()
library.borrow_book('Python 101')
library.borrow_book('Java 102')
library.show_books()
library.return_book('Python 101')
library.return_book("Java 101")
library.return_book("Java 102")
library.show_books()