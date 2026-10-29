class vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

class Bus(vehicle):
    def __init__(self, seating_capacity):
        super().__init__(seating_capacity)

    def fare (self):
        base_fare = self.seating_capacity * 100
        return base_fare + (base_fare * 0.10)

school_bus = Bus(50)
print ("The bus fare is : " , school_bus.fare())