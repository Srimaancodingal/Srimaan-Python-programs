num = int (input ("Enter a number : "))
binary_number = 0
place_value = 1 
while num > 0:
    remainder = num%2
    binary_number = binary_number + (remainder * place_value)
    place_value = place_value * 10 
    num = num // 2
print (binary_number)