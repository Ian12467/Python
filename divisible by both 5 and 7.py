#CHECK WHETHER A NUMBER IS DIVISIBLE BY both 5 and 7
number=int(input("Enter number:"))
if number%5==0 and number%7==0:
  print("divisible by both 5 and 7")
else:
  print("number is not divisible by 5 and 7")