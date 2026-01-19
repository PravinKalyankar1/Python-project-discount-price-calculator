# String indexing
name= "Pravin"
print(name)
print(name[4])
print(name[-3])

#string Slicing
product="Laptop pro 2024"
print(product[-4:])

text="DataAnalysis"
print(text[0:4]) # Extracting first 4 letter (Data)
print(text[-4:])
print(text[0:12])# Extracting all letter forward
print(text[-12:]) # Extracting all letter reverse
print (text[4:12]) # Extracting analysis word
print(text[4:]) # Extracting analsis word
print (text[:4]) # Data
print(text[-6:])# alysis

# Skip text Datananlysis by 1 word
print("Skip text:", text[0:12:2])
print ("Skip text:", text[0:12:3])

# Reverse string
print("Reverse string:",text[::-1])
print("Revers data word:", text[3::-1])

name="Rohit"
print("Name:",name[0:5])