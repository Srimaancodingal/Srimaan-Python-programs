import random 
import string 

p1 = string.ascii_lowercase
p2 = string.ascii_uppercase
p3 = string.digits
p4 = string.punctuation

print ("%^****WELCOME TO PASSWORD GENERATOR&^%****")
x = int(input("Enter Number of characters :"))

all_chars = (p1+p2+p3+p4)
password = ""

for i in range(x):
    password += random.choice(all_chars)

print ("Your password is", password)
