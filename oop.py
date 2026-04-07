class Book:
    """ A class to model a bool """
    title = " Alchemist"
    author = "Poulo Coelho"  
    genre = "Fiction"
    
    def describe_book():
        print("Describing Book...")
    
book = Book()
print(book.author)