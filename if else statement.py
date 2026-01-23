# if-else conditions

age=int(input("Enter your age:"))

if age>=18:
    print("Adult")
else:
    print("Minor")  
      
# Discount checker

amount=900
if amount>=1500:
    print("You will get 10% Discount")
else:
    print("No Discount")
    
# if-elif-else condition
Marks=int(input("Enter your marks:"))

if Marks>=90:
    print("Grade'A'")    
elif Marks>=60:
    print("Grade'B'")  
elif Marks>=35:
    print("Grade'C'")
else:
    print("Fail....!")  
    
# Sales performance (Data Analystusecase)
sales=124000
if sales>=100000:
    print("High performance")
elif sales >=50000:
    print("Medium performance")
else:
    print("Low performance")

# Password checking 
password=input("Enter your password:")
if password=="Admin@123":
    print("Login Sucessful")
else:
    print("Wrong Password")

# Converting password to lower
password=input("Enter your password:")
if password.lower()=="admin@123":
    print("Login sucessful")
else:
    print("Password wrong")

#Email Validation

email="user@example.com"
if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
    
# Advanced missing data checking

value= " "
if value== " hdhdh":
    print("Data missing")
else:
    print("Data Availble") 