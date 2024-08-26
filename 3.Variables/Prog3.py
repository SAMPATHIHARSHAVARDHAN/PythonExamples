#dynamical type casting
froot_name=input("Enter Froot Name")
qty=int(input("Enter Qty"))
rate=float(input("Enter Unit Price"))
totalamount=qty*rate
print("Froot Name " + froot_name + " Qty " + str(qty) +
      " Unit Price" + str(rate) + " Total Amount is "
      + str(totalamount))

#whiel calculation only type casting

froot_name=input("Enter Froot Name")
qty=input("Enter Qty")
rate=input("Enter Unit Price")
totalamount=int(qty)*float(rate)
print("Froot Name " + froot_name + " Qty " + qty
      + " Unit Price" + rate + " Total Amount is "
      + str(totalamount))