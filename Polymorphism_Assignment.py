class Tesla:
    def fuel_type(self):
        print ("Tesla uses Battery Power")
    def max_speed (self):
        print ("Max speed of Tesla is 200 kmph")
    



class Ferrari:
    def fuel_type(self):
        print ("Ferrari uses Petrol Power")
    def max_speed (self):
        print ("Max speed of Ferrai is 500 kmph")

tsl = Tesla()
fri = Ferrari()

for i in (tsl, fri):
    i.fuel_type()
    i.max_speed()