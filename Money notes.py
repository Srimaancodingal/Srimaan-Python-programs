Amount = int (input("Enter the amount of money you have: "))
note_100 = Amount // 100
note_50 = (Amount % 100) // 50
note_10 = (Amount % 100) % 50 // 10
print ("The number of 100 notes is: ", note_100)
print ("The number of 50 notes is: ", note_50)
print ("The number of 10 notes is: ", note_10)