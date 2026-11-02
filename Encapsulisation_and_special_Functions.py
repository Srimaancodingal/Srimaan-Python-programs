class reverse:
    def __init__(self, s):
        self.s = s 
    def rvrstr (self):
        return self.s [::-1]

word = input("Enter your word please")
ob = reverse (word)
print ("The reversed version ", ob.rvrstr ())
  