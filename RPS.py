import random
ch = ["rock , paper scissor"]
computer_ch = random.choice(ch)
print ("****** WELCOME TO ROCK | PAPER | SCISSOR *********")
player_ch = input("Enter choice : ").lower()
print ("Player choice is", player_ch)
print ("Computer choice is", computer_ch)
if player_ch == computer_ch:
    print ("It is a Tie ")
elif player_ch == "rock" and computer_ch == "scissor":
    print ("YOU WON!")
    print ("==========================================================")
elif player_ch == "scissor" and computer_ch == "paper":
    print ("YOU WON!")
    print ("==========================================================")
elif player_ch == "paper" and computer_ch == "rock":
    print ("YOU WON!")
    print ("==========================================================")    
else:
    print ("Computer Wins")