purchase_price = int(input("Enter the purchase price: "))
Selling_price = int(input("Enter the selling price: "))
if Selling_price > purchase_price: 
    profit = Selling_price - purchase_price
    print ("Profit is", profit)
else:
    loss = purchase_price - Selling_price
    print ("Loss is", loss)