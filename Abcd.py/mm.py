Units=int (input("Enter the amount of units"))
if Units<=50:
    amount = Units * 2.60
    tax= 25
elif Units<=100:
    amount = Units * 3.25
    tax = 35
elif Units<=200:
    amount = Units * 5.26
    tax = 45
else:
    amount = Units * 8.45
    tax = 75
print (" Electricity bill = ", amount + tax )


