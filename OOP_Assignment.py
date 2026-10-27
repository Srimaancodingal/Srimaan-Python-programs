class animal: 
    def __init__(self, breed, colour):
        self.breed = breed 
        self.colour = colour

    def display(self): 
        print(f"This is a {self.breed} and it is {self.colour}.")

ob1 = animal("Pomerian", "White")
ob1.display() 

ob2 = animal("German Shepherd", "Brown Tan")
ob2.display()