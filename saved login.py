#program to login
username=str(input("Enter username: "))#user enter username 
pwd=int(input("Enter password: "))#user enter password
logins=["BSCIT-05-025/20",123]
if username in logins and pwd in logins:
  print("login successful")
else:
  print("login not successful")