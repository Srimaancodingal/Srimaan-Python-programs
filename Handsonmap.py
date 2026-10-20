num1 = [1,2,3,4,5]
num2 = [6,7,8,9,10]

Add = map(lambda x , y: x + y, num1 , num2)
print (list(Add))

def sq(n):
    return  n * n

result = list(map(sq , num2))
print (result )
