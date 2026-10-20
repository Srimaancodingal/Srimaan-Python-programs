s1 = {"A", "B", "C"}
s2 = {4,5,7}
s3 = list(zip(s1,s2))
print (s3)

list1 = [10,20,30,40,50]
list2 = [100,200,300,400,500]
for x, y in zip(list1, list2 [::-1]): 
    print (x,y)

product = ['Chocolate', 'Cake', 'chips']
prices = [150, 400, 60]
my_dict = {product: prices for product, prices in zip(product, prices) }
print (my_dict)