#Grading system in python language
print("-----------------------------------------------")
print("-----------------------------------------------")
print("###############################################")
print("  THE  GRADING  SYSTEM  OF  ZETECH UNIVERSITY  ")
print("***********************************************")
print("-----------------------------------------------")
#Prompt the user to enter subject names
subject1=str(input("Enter first subject name: "))
subject2=str(input("Enter second subject name: "))
subject3=str(input("Enter third subject name: "))
subject4=str(input("Enter forth subject name: "))
subject5=str(input("Enter fifth subject name: "))
#Prompt the user to enter subject marks
marks1=float(input (subject1+" = "))
marks2=float(input (subject2+" = "))
marks3=float(input (subject3+" = "))
marks4=float(input (subject4+" = "))
marks5=float(input (subject5+" = "))
#Calculates and print out the total marks scored by the student
total=marks1+marks2+marks3+marks4+marks5
total=str(total)#type-conversion of total from float to string
print("Total score of the student is "+total+" marks")
total=float(total)#type-conversion of total from string to float
average=total/5#calculates the average marks
average=str(average)#type-conversion
print("The average is "+average+" marks")#concatenation
average=float(average)#type-conversion
#Condtional statements are implemented
#The if, elif and the else statement
if average>=70 and average<=100:
  print("you have scored grade A")
elif average>=60 and average<=69:
  print("you have scored grade B")
elif average>=50 and average<=59:
  print("you have scored grade C")
elif average>=40 and average<=49:
  print("you have scored grade D")
elif average>=30 and average<=39:
  print("you have scored grade E")
else:
  print("You have failed")
print("-----------------------------------------------")
print("***********************************************")
print(" THANK  YOU  FOR  USING  THE  GRADING  SYSTEM  ")
print("###############################################")
print("-----------------------------------------------")
print("-----------------------------------------------")
  #End of the program