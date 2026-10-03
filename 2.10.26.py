try:
    age = int(input("ENTER AGE : "))
except ValueError:
    print ("Please enter a valid age ")
if age % 2 == 0:
    print ("The age is even")
else:
 print ("The age is odd")