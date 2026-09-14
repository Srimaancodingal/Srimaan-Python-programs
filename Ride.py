print("Select your ride: ")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("What type of bike?")
    print("1. Scooty")
    print("2. Motor bike")
    choice2 = int(input("Enter your choice2: "))
    
    if choice2 == 1:
        print("You have chosen Scooty")
    else:
        print("You have chosen Motor bike")

elif choice == 2:
    print("What type of car?")
    print("1. SUV")
    print("2. Suzuki")
    choice3 = int(input("Enter your choice3: "))
    
    if choice3 == 1:
        print("You have chosen SUV")
    else:
        print("You have chosen Suzuki")

else:
    print("Invalid choice! Please select 1 or 2.")