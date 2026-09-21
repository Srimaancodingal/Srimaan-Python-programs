row = int(input("Enter the row : "))

for i in range(1, row+1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()

for i in range(row, 1, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()