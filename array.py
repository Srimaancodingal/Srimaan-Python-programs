import array as arr
array_num = arr.array ('i', [1,2,3,4,5,6,2,2,3,4,1])

print ("Occurence of number 2 : " +str(array_num.count(2)))
array_num.reverse()
print (array_num)