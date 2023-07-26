# BASE CLASS
class Animal():

    def __init__(self):
        print('ANIMAL CREATED')

    def who_am_i(self):
        print('ANIMAL')

    def eat(self):
        print('EATING')


# INHERITED CLASS FROM ANIMAL
class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('DOG CREATED')

    def bark(self):
        print('WOOF WOOF!')

    def eat(self):
        print('DOG EATING')

dog = Dog()
dog.who_am_i() # Result : ANIMAL
dog.eat() # Result : DOG EATING
dog.bark() # Result : WOOF WOOF!