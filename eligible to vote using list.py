 #check if a person is eligible to vote
nationality=input("Enter Nationality: ")
age=int(input("Enter age: "))
country=["kenya","uganda","tanzania"]
if nationality.lower() in country and age>=18:
  print("ELIGIBLE TO VOTE")
else:
  print("NOT ELIGIBLE TO VOTE")


