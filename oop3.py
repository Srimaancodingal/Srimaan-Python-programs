class parrot:
    species = "bird"
    def __init__(self, name, age):
        self.name = name
        self.age = age 

blu = parrot("blu", 5)
woo = parrot("woo", 7)

print (blu.name, "is a", blu.species, "and is", blu.age, "years old")
print (woo.name, "is a", woo.species, "and is", woo.age, "years old")
