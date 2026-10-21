print ("1. Filtering Numbers") 
numbers = [1,2,3,4,5,6,7,8,9,10]
lst1 = [x for x in numbers if x%2 == 0 ]
print ("The list of even numbers : ", lst1)

lst2 = [x for x in numbers if x%2 != 0]
print ("The list of odd numbers : ", lst2 )

print ("2.Capitalizing letters of fruit names")

Fruit_Names = ["Strawberry", "Mango", "Rasberry"]
Capitalize_Names = [f.capitalize () for f in Fruit_Names]
print (Capitalize_Names)
