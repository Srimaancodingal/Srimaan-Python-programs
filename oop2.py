class vehicles:
    def __init__(self , max_speed , mileage):
        self.max_speed = max_speed
        self.mileage = mileage 
ob = vehicles(300,50)

print ("The max_speed is", ob.max_speed)
print ("The mileage is", ob.mileage)
