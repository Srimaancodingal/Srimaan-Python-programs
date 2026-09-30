try:
    num1= int(input("Enter num1 : "))
    num2= int(input("Enter num2 : "))
    result = num1/num2
    print (result)
except ValueError:
    print ("Enter valid value")
except ZeroDivisionError:
    print ("Can't be devided by 0")
except:
    print ("Exception")
finally:
    print ("The statement will be printed at any cost")
print ("Satement after code")