from abc import ABC, abstractmethod 

class Abstractclass (ABC):
    def Display (self, a):
        print ("The value is", a)

    @abstractmethod
    def abs_method ():
        print ("This is an abstract")

class childclass(Abstractclass):
    def abs_method(self):
        print ("This is an implemented method")

ob = childclass()
ob.Display(10)
ob.abs_method ()