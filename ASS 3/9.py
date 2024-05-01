#1) A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.

unitcost = 100
quantity = int(input("Enter the quantity: "))
totalcost = quantity * unitcost

if totalcost > 1000:
    discount = totalcost * 0.1
    totalcost -= discount

print("Total cost:", totalcost)
