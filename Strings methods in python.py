# String Methods
# Remove spaces
text= "          Hello python  learners.     "
print("Original text:", text)
print("Remove sapace:", text. strip())

print("Capital letters:", text. upper(). strip()) # Convert to capital & remove space

# Convert to propercase

print("Proper case:", text. title().strip())

# Convert to lowercase

print("Lower case:", text. lower().strip())

# Replace word
print("Replace python with sql:", text.replace("python", "Sql").strip())
    
    # count occurrence of a letter of word
    
print("Count of o word:", text. count("o"))

# Check if text start with something

print("Start with Hello:", text.strip().startswith("Hello"))

# Check numbers are present in data
mobile_no=4645337364
print("Is numeric:", mobile_no.is_integer()) # True
mobile_no="dddshdsdgygd"
print("Is numeric:", mobile_no.isnumeric()) # False

# Split the string into number of words
msg="Welcome to python course"
words= msg.split()
print("World list:" , words)

#  Joined words
joined_text= "-".join(words)
print("Joined words:", joined_text)

# Indexing of word
text1= "Welcome to Python"
print("Index of P:", text1.find("P"))

# Extract domain
email= "Student@example.com"
domain=email[email.find("@")+1:]
print("Domain:", domain)

