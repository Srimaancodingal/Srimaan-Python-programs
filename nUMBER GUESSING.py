import random 
computer_ch = random.randint (1 , 20)
print ("Welcome to Number guessing game ")
while True:
    user_ch = int(input("Enter Number"))
    if user_ch == computer_ch:
        print ("Congratulations 😊😊 your guess is correct")
        break
    elif user_ch > computer_ch:
        print ("Too high! Try again")
    elif user_ch < computer_ch:
        print ("Too low! Try again")
        