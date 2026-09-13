import random
secret_number = random.randint(1, 10) 

while True:
    Player_Guess = int(input("Make your guess from 1 to 10: "))
    if Player_Guess == secret_number:
        print("Yay! your guess is right'😊")
        break
    else:
        print("OOPS! 😔 YOUR GUESS IS WRONG")
        print ("Secret_Number")
        