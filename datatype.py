# 1 Text data type 
# string
customer_name="Pravin"      
print("customer name is :", customer_name)
print("Customer data type is:", type(customer_name))
# 2 integer
Salary=25000
print("Employee salary:",Salary)
print ("Employee salary data type is:", type(Salary))

# Numeric data type
# 2.1 Integer complete number
rating=4
order_quantity= 5
print("Rating the data type:", type(rating))
print("Order quantity data type:", type(order_quantity))
#2. 2 Float - Decimal number
order_amount= 8999.90
print("order_amount data type:", type(order_amount))
#2.3 complex number
a=3+2j
print(type(a))
# 3 Boolean - True/False
is_paid=True
print(is_paid,type(is_paid))
# 4 Sequence
# 4.1 List 
cities= ["Mumbai","Delhi", "Kolkata", "Chennai"]
print(cities)
print(type(cities))
#4.2 Tuples
dimensions=(1000,1900)
print(dimensions)
print(type(dimensions))
#4.3 Range
num= range(1,11)
print(list(num))
print(type(num))
# Dictonary(dict)
student= {"name": "Anvi",
          "age":25,
          "city":"Mumbai"
        }
print(student)
print(type(student))
# 6 Set
numbers= {1,2,3,4,5,5,7,7,7,9,9,8,8,0,0}
print(numbers, type(numbers))
print(type(numbers))
numbers=[1,4,9,0,8,8,9]
print(numbers, type(numbers))
# 7 Remarks
remarks= None
print(remarks, type(remarks))

