import re
email_condition="^[a-z]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter the Email:")
if re.search(email_condition,user_email):
   print("correct email id.")
else:
   print("wrong email id.")