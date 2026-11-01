class my_class:
    __privatevar = 20

    def __priv_meth (self):
        print ("I'm in class called my class")

    def hello(self):
        print ("The private variable is", my_class.__privatevar)

ob = my_class()
ob.hello()
ob.__priv_meth()
