class vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage 

class Bus(vehicle):
    pass
obj =Bus("Vrs Bus", 40, 25)
print ("The name is", obj.name)
print ("The maximum speed is", obj.max_speed)
print ("The mileage is", obj.mileage)

    