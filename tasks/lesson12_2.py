"""
Library

Write a class structure that implements a library. Classes:
1) Library - name, books = [], authors = []
2) Book - name, year, author (author must be an instance of Author class)
3) Author - name, country, birthday, books = []

Library class

Methods:
- new_book(name: str, year: int, author: Author) - returns an instance of Book
    class and adds the book to the books list for the current library.
- group_by_author(author: Author) - returns a list of all books grouped
    by the specified author
- group_by_year(year: int) - returns a list of all the books grouped by the specified year

All 3 classes must have a readable __repr__ and __str__ methods.

Also, the book class should have a class variable which holds the amount of all existing books
"""
import datetime as dt


class Author:
    def __init__(self, name, country, birthday):
        self.name = name
        self.country = country
        self.birthday = birthday
        self.books = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Author name={self.name} country={self.country}>"


class Book:
    def __init__(self, name, year, author):
        if not isinstance(author, Author):
            raise ValueError("Should be an instance of Author class")

        self.name = name
        self.year = year
        self.author = author

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Book name={self.name} year={self.year}>"


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        self.authors = []

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Library name={self.name}>"

    def new_book(self, name, year, author):
        if not isinstance(author, Author):
            raise ValueError("Should be an instance of Author class")

        book = Book(name, year, author)

        self.books.append(book)

        return book

    def get_by_author(self, author):
        return [book for book in self.books if book.author.name == author.name]

    def get_by_year(self, year):
        return [book for book in self.books if book.year == year]


central_library = Library("Central Library")

author1 = Author("Fyodor Dostoyevsky", "Russian Empire", "November 11, 1821")
author2 = Author("J.R.R. Tolkien", "South Africa", "January 03, 1892")

central_library.new_book("Crime and Punishment", 1866, author1)
central_library.new_book("The Fellowship of the Ring", 1954, author2)

print(central_library)

# for book in central_library.books:
for book in central_library.get_by_author(author1):
    print("{} by {}, {}".format(
        book.name,
        book.author.name,
        book.year
    ))
