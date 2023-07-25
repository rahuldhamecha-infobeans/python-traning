def first_function(param = 'default'):
    """
    This is functions demo doc String.
    :arg param:
    :return:
    """
    print("This is my first function demo!. {}".format(param))

# first_function('Rahul')

def add_numbers(num1,num2):
    """
    To Perform the addition of the 2 numbers.
    :param num1:
    :param num2:
    :return:
    """
    return num1+num2

print(add_numbers(4,5))

# FITLER Function

def find_evens(num):
    return num%2 == 0

my_list = [1,2,3,4,5,6,7,8,9,10,20,41,51]

evens = filter(lambda num: num%2 == 0,my_list)

print(list(evens ))