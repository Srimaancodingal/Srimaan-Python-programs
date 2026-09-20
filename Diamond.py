rows = int(input("Enter rows : "))
if rows % 2 == 0:
    halfdiamond = int(rows/2)
else :
    halfdiamond = int(rows/2)+1
space = halfdiamond -1
 #upper diamond
for i in range (1, halfdiamond+1):
    for j in range (1, space +1):
        print (end = " ")
    space = space-1
    num = 1 
    for k in range (2*i-1):
        print (end = str (num))
        num = num+1 
    print ()
space = 1 
for i in range (1, halfdiamond+1):
    for j in range (1, space +1):
        print (end = " ")
    space = space+1
    num = 1 
    for k in range (1, 2* (halfdiamond-i)):
        print (end = str (num))
        num = num+1
    print ()

