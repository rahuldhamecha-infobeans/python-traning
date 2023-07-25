# STRINGS

# Basics
name = 'RahulDhamecha'
name = "RahulDhamecha"

# Indexing
print("Indexing : ")
print(name[2])
print("  ")

# Slicing
print("Slicing : ")
print(name[5:])  # Return the string from the 5th character "Dhamecha"
print(name[:5])  # Return the string upto the 5 character "Rahul"
print(name[5:9]) # Return the 5 : 9 character string "Dham"
print(name[::2]) # Return every second element from the string "Rhlhmca"
print("  ")

# Basic Methods
print("Basic Methods : ")
upper = name.upper() # Convert into upper case "RAHULDHAMECHA"
print(upper)

lower = name.lower() # Convert into lower case "rahuldhamecha"
print(lower);

split = name.split('h') # Convert into array by splitting h "['Ra', 'ulD', 'amec', 'a']"
print(split)
print("  ")

# Print Formatting
item_one = 'dog'
item_two = 'cat'
x = "Item One : {}, Item Two : {}".format(item_one,item_two)
print(x)