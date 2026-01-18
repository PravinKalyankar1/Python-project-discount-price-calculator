# Input and typecasting

name= input("Enter your name:")
print("Welcome", name)
age=input("Enter youy age:")
print("Your age is:", age)
print(type(age))

# Typecasting
age=int(input("Enter your age:")) # Here changing the data type str to int
print("Your age is:", age)
age=age+5
print(age)
print(type(age))

temperature=input("Enter today's temp:")
print("Today's temp :", temperature)
print(type(temperature))
temperature=float(input("Today's temp :"))
print("Today's  temp :", temperature)
print(type(temperature))

# Convert number to string
sales=50000
text="Total sales:" + str(sales)
print(text)
print(type(text))

# Total sales calculator
product=input("Enter your product name:")
quantity=int(input("Enter your quantity sold:"))
price_per_unit= float(input("Enter price per unit ₹:"))
total_sales= quantity*price_per_unit
print("*********************************")
# print("product:", product)

print("Total sales amount(₹):", total_sales)

# Addtion calculator
name1="Paneer_tika(₹):"
name2="Roti(₹):"
First_value= int(input(name1))
Second_value= int(input(name2))
Your_bill= First_value+Second_value
print("Your_bill(₹):", Your_bill)

# Substraction
first_number=float(input("Enter the first number:"))
second_number=float(input("Enter the second number:"))
substraction= first_number - second_number
print("Substraction:",substraction)

# Employee salary slip

Employee_name= input("Employee Name:")
Employee_Salary=int(input("Enter the employee salary:"))
Employee_code=int(input("Enter the Employee code:"))
Employee_Bonus=int(input("Enter the bonus amount:"))
Tax=float((input("Enter tax %:")))

Gross_salary= Employee_Salary + Employee_Bonus
tax_amount= Gross_salary * (Tax/100)
net_salary= Gross_salary-tax_amount

print("-----Salary Slip-----")
print("Employee:", Employee_name)
print("Employee Code:", Employee_code)
print("Gross salary:", Gross_salary)
print("Tax:", tax_amount)
print("Net Salary:", net_salary)