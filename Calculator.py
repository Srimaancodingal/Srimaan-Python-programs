def Add (num1 , num2):
    return num1 + num2 
def sub (num1 , num2):
    return num1 - num2 
def mul (num1 , num2):
    return num1 * num2 
def div (num1 , num2):
    return num1 / num2 
print ("======================CALCULATOR===============================")
print ("1. Addition")
print ("1. Subtraction")
print ("1. Multipliction")
print ("1. Division")
ch = int(input("Enter the Operation"))
num1 = int(input("Enter number 1 : "))
num2 = int(input("Enter number 2 : "))
if ch == 1:
    print ("Addition of number 1", num1 , " and ", num2 , " is ", Add (num1 , num2))
elif ch == 2:
     print ("Difference of number 1", num1 , " and ", num2 , " is ", sub (num1 , num2))
elif ch == 3:
     print ("Product of number 1", num1 , " and ", num2 , " is ", mul (num1 , num2))
elif ch == 4:
     print ("Quotient of number 1", num1 , " and ", num2 , " is ", div (num1 , num2))

