while True:
    try:
        num_1 = int(input("Enter number-1 : "))
        break
    except ValueError:
        print("Invalid input for Number 1. Please enter a whole number.")

while True:
    try:
        num_2 = int(input("Enter number-2 : "))
        break
    except ValueError:
        print("Invalid input for Number 2. Please enter a whole number.")

operation = input("Operation to be performed (+, -, *, /, %): ")

if operation == "+":
    result = num_1 + num_2
    print(result)

elif operation == "-":
    result = num_1 - num_2
    print(result)

elif operation == "*":
    result = num_1 * num_2
    print(result)

elif operation == "/":
    result = num_1 / num_2
    print(result)

elif operation == "%":
    result = num_1 % num_2
    print(result)

else:
    print("Invalid operation. Please choose from +, -, *, /, or %.")