def cube(num):
    return num ** 3
def cube2(num):
    if num % 3 == 0:
        return cube(num)
    else :
        return False

print (cube2 (2004))