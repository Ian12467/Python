#program to assign discount
purchase=int(input("Enter amount:"))
discount=5/100
discount=purchase*discount
pay=purchase-discount
if purchase>1000:
  print("Purchase: ",purchase)
  print("Discount: ",discount)
  print("Pay: ",pay)
else:
  print("not discounted")
