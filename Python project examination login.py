# # ASSIGNMENT  — Online Exam Login

reg = int(input("Enter registration number: "))

if reg == 1221:
    subject = input("Enter exam subject: ")

    if subject.lower() == "python":
        password = int(input("Enter exam password: "))

        if password == 8888:
            print("Login successful! Start your exam.")
        else:
            print("Wrong password.")
    else:
        print("Subject not available.")
else:
    print("Registration failed.")

