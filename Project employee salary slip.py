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