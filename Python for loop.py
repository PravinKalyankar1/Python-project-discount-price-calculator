# For loop

# Basic loop
for i in range(0,10):
    
    print (i)

# Print characters

word="Python"
for alaphabet in word:
    print(alaphabet)
    
word2="SQL"
for j in range(0,11):
    print(word2)
    
# Loop through list

items= ["pen","books","Papers", "Laptop"]
for item in items:
    print(item)
# Even numbers
for n in range(0,21,2):  # even number 0-20
    print(n)    
    
# Odd numbers
for n in range (1,21,2): # odd number 0-20
    print(n)             
    
# Total calculations
marks= [78,776,98]
total=0
for m in marks:
    total+=m
    print("Total:", total)
 # clean city names
 
Cities = [" Mumbai", "pune ","  CHENNAI" ]   
cleaned= []
for c in Cities:
    cleaned.append(c.strip().title())
    print(cleaned) 
    
 # loop with if condition
nums = [5,12,3,18,7]   
 
for n in nums:
     if n > 10:
         print(n, "is greater than 10")
     else:
         print(n, "is not greater than 10")

#     for n in nums       
     nums = [5,12,3,18,7]   
 
for n in nums:
     if n % 2==0:
         print(n, "- Even Number")
     else:
         print(n, "- Odd Number")     
#9 Extract last digit from ids
ids= ["Emp- 001122", "Emp- 889900"]
for last4 in ids:
    print(last4[-4:])         
    # Key value on dictionary
student={"name":"Pravin", "age":25, "city":"Pune"}
for key, value in student.items():
        print(key,":",value)