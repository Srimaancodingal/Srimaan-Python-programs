import random
computer_ch = random.randint(1 , 6)
player_ch = int(input("Enter the Number you've got : "))
print ("*********** WELCOME TO ROLL A DIE ***************")
if computer_ch == player_ch:
    print ("It is a Tie ")
print ("--------------------------------------------")
if computer_ch > player_ch:
    print ("YOU WIN!!")
print ("--------------------------------------------")
if computer_ch < player_ch:
    print ("OOPS! you lost (Computer Wins) ")
