# IF Condition Check
a = 3;
if a<5:
    print("First block Demo")
    if a>2:
        print("Second Block Demo")


# FOR Looop
list = [1,2,3,4,5,6,7,8,9,10]
for item in list:
    print("Hello World {}".format(item))

# While Loop
i = 0
while i<5:
    print("I is {}".format(i))
    i = i + 1

for item in range(0,20,5):
    print(item)

power = [1,2,3,4,5,6,7,8,9,10]

power_value = [num**2 for num in power]
print(power_value)