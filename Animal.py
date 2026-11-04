from abc import ABC, abstractmethod

class Animal (ABC):
    def move(self):
        pass

class Human (Animal):
    def move (self):
        print ("Human can walk")

class Snake (Animal):
    def move (self):
        print ("Snake can slither")

class dog (Animal):
    def move (self):
        print ("Dog can bark")

h = Human()
h.move()

s = Snake()
s.move()

d = dog()
d.move()