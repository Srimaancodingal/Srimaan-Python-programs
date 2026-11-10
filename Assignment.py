class book :
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False
    def borrow(self):
        if self.is_borrowed == False:
            self.is_borrowed = True
            print("Borrow confirmed")
        else:
             print("Already borrowed")

    def return_book(self):
         
        if self.is_borrowed == True:
            self.is_borrowed = False 
            print("Book returned successfully")
        else:
            print("This book was not borrowed")

    def __str__ (self ):
               
        if self.is_borrowed:
            status = "Borrowed"
        else:
            status = "Available"
        return f"{self.title} by {self.author} [{status}]"

book1 = book("The Hobbit", "J.R.R. Tolkien")
book2 = book("1984", "George Orwell")


print(book1)

book1.borrow()
book1.borrow() 




