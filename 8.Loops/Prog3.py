cum_amount=0
amount=int(input("Enter Amount"))
while amount>0:
    cum_amount=cum_amount+amount
    amount = int(input("Enter Amount"))
else:
    print("Bill Counter is Close :")
print(f"The total Amount is {cum_amount}")
