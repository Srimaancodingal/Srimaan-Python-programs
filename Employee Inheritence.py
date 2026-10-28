class person:
    def __init__(self, name, id_number, salary):
        self.name = name
        self.id_number = id_number
        self.salary = salary 
    def display (self):
        print (self.name)
        print (self.id_number)
        print (self.salary)
class Employee(person):
    def __init__(self, name, id_number, salary, post):
        self.post = post 
        super().__init__(name, id_number, salary)
        
obj = Employee("Srimaan", 12015, 500000, "Developer")
obj.display ()



