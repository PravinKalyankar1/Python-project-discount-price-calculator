# 1. Meeting login 

security_code = int(input("Enter the security code: "))

if security_code == 5566:
    department = input("Enter your department: ")

    if department.lower() == "finance":
        access_level = int(input("Enter your access level: "))

        if access_level >= 5:
            print("Access Granted: Welcome to the meeting room.")
        else:
            print("Insufficient access level.")
    else:
        print("Access denied: Department not allowed.")
else:
    print("Invalid security code.")
