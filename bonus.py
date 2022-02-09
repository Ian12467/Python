#program to calculate bonus
salary=float(input("Enter salary: "))#user enter salary 
time=int(input("Enter years of service: "))#user enter years
if time>10:#checks if time is more than 10 years
  bonus=salary*10/100
  print("Net bonus is ",bonus)
'''checks if time is greater or equal to 6 and less or equal to 10 years'''
if time>=6 and time<=10:
  bonus=salary*8/100
  print("Net bonus is ",bonus)
else:
  bonus=salary*5/100#checks if time is less than 6 years
  print("Net bonus is ",bonus)