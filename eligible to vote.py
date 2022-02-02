#check if a person is eligible to vote
nationality=input("Enter Nationality: ").lower()
age=int(input("Enter age: "))
if nationality=="kenyan" or nationality=="Sudan" and age>=18:
 
  print("ELIGIBLE TO VOTE")
else:
  print("NOT ELIGIBLE TO VOTE")


