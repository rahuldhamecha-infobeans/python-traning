# Global Scope
name = 'Rahul Dhamecha'

# Enclosing function locals
def greet():
    # Local function scope
    name = "Darsh Shah"
    def hello():
        print("Hello {}".format(name))

    hello()

greet() # Result : Hello Darsh Shah

# Override global variable using global keyword
def rename():
    global name
    name = "Hemanshu Dhamecha"

print("Before the Rename function call,  name is : ",name) # Result : Before the Rename function call,  name is :  Rahul Dhamecha
rename()
print("After the Rename function call,  name is : ",name) # After the Rename function call,  name is :  Hemanshu Dhamecha