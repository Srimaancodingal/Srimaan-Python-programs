class Computer:
  def __init__(self):
    self.__maxprice = 800
  def sell(self) :
    print ("Original selling price", self.__maxprice)
  def setmaxprice (self, price):
     self.__maxprice = price

ob = Computer()
ob.sell ()

ob.__maxprice = 1000
ob.sell ()

ob.setmaxprice(6000)
ob.sell()

