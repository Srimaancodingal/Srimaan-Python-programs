class IOStream: 
    def __init__(self):
        self.str1 = ""

    def get_string(self):
        self.str1 = input("Enter string : ")

    def print_string(self):
        print ("String in uppercase", self.str1.upper())

ob = IOStream()
ob.get_string()
ob.print_string()