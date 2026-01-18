# Operators
# Arithmatic operators
num1=40
num2=3
print(num1-num2)  # Substration
print (num1 + num2) # Addtion
print (num1 * num2) # Multiplication
print (num1/num2) # Dividation
print (num1 % num2) # Modulas
print (num1**num2) # Exponenet(power)
print (num1 // num2) # Floor divison

# Assignment operators
x=5   # assignemet operator
print (x)
x+=10 # add 10
print (x)
x-=10 # subtract 10 from all 
print(x)
x=10 # Here again assign x=10
x*=10 # multiplication with 10
print(x)
x=x/2
print(x)
# Comparators operators
p1=20
p2=40
print(p1 < p2) # Less than true condition
print (p2 > p1) # Greater than true condition
print(p1>p2) # False condition
p3=20
p4=20
print(p3==p4) # Equal to true condition
print (p3!=p4) # Not equal to False
p5=60
p6=70
print(p5!=p6) # Not equal to true condition
print(p5==p6) # equal to false 

# Logical operators
x1=5
x2=15
x3=30
x4=40
print("And condition:", x1< x2 and x3 < x4) # And Condition if all true then true
print("Or condition:", x1>x2 or x3<x4) # Or condition if anyone true then true
print (x1>x2 and x3<x4)# if anyone is false all false
print(x1>x2 or x3>x4)# if all false false 
print (not 5>3) # not condition resverse the output
print(not 5>30) # revesre the output

# Identity Operators
x1=100
x2=100
print (x1 is x2) # true conditiom
print (x1 is not x2)# false condition
x3= 100
x4= 105
print (x3 is x4) # false condition
print (x3 is not x4) # true condition

# Membership operator
print ("check 'e' in mango:", 'e' in 'mango')
print ("check 'a'in mango", 'a'in 'mango')
print ("check 'a' not in apple:", 'a' not in 'apple')