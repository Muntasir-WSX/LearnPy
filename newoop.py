class Book:
    def __init__(self, title, author, genre):
        self.title = (title,)
        self.author = (author,)
        self.genre = (genre,)

    def read_book(self):
        print(f"Reading {self.title[0]} by {self.author[0]} in the {self.genre[0]} genre.")
        
    def describe_book(self):
        print(f"{self.title[0]} is a {self.genre[0]} book written by {self.author[0]}.")
        
    def __str__(self):
        return f"Book(title='{self.title[0]}', author='{self.author[0]}', genre='{self.genre[0]}')" 

book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", "Science Fiction")
print(book.read_book())
print(book.describe_book())
