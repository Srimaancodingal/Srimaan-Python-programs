num= int (input("Enter your number"))
if not num %2 ==0:
    print ("Number is divisible but reversing because of not operator")
else: 
   print ("Number is not divisible but reversing because of not operator")
if num % 2 == 0 and num % 3 ==0 :
    print ("Number is divisible by both the numbers")
else:
    print ("Number is not divisible by atleast one number")

num= int (input("Enter your number")) 
if num % 2 == 0 or num % 3 ==0 :
    print ("Number is divisible atleast one number")
else:
    print ("Number is not divisible by both the numbers")
