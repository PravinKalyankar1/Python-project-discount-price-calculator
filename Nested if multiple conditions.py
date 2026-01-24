print("check your eligibility")

age=int(input("Enter your age:"))

if age>=18:
    id_no=int(input("Enter your id:"))
    if id_no == 1000:
        print("You can enter")
    else:
        print("Wrong Id")
else:
    print("Your are underage")

# Multiple conditions(and)
age=int(input("Enter your age:"))
residence=input("Are you indian?")
if age>=18 and residence.lower()=="yes":
    print("Your are eligible")
else:
    print("Your are not eligible")
        
# Multiple conditions(Or)
age=int(input("Enter your age:"))
residence=input("Do you have Licence:")
if age>=18 or residence.lower()=="yes":
    print("You are eligible to register")
else:
    print("You are not eligible")    
