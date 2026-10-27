class pair_element:
    def two_sums(nums , target):
        lookup = {}

        for i , num in enumerate(nums):
            if target - num in lookup : 
                return lookup[target - num]- i
            lookup  [num] = i
e = int(input("Enter Target : "))
print ("index-1 = %d Index-2 = %d "% pair_element (). two_sums ((10,20,30,40,50,60,70), e))
            


    