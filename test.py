class book:
    def __init__(self, title, author):
      self.title = title
      self.author = author 
      is_borrowed = False 

    def borrow(self, title, author):
        self.title = title
        self.author= author 
        is_borrowed = True 
        print ("Borrow confirmed")

    def return_book (self, title, author):
        self.title = title 
        self.author = author 
        is_borrowed = False 
        print ("Book returned")

ob1 = book("Alice wonder land", "John")
ob2 = book("Diaryof a wimpy kid", "Greg")
ob3 = book("A journey through himalayas", "Sudha Murthy")

ob1.borrow(ob1.title, ob1.author)
ob1.return_book(ob1.title, ob1.author)

ob2.borrow(ob2.title, ob2.author)
ob2.return_book(ob2.title, ob2.author)


ob3.borrow(ob3.title, ob3.author)
ob3.return_book(ob3.title, ob3.author)



