try:
    num1 = int(input("Enter number : "))
    print (num1)
except ValueError as ex:
    print ("Exception", ex)
