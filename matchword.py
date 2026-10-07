def match_word (L):
    lst = []
    count = 0
    for i in L:
        if len(i)>1 and i [0] == i [-1]:
            count = count +1
            lst.append (i)
    print ("The list is : ", lst)
    return count

call = match_word (["aba" , "ccc" , "Hannah" , "lak" , "oop" , "kjkh"])
print (call)
