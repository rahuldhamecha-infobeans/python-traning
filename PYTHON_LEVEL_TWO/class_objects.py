class Circle():
    pi = 3.14
    def __init__(self,radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self,new_radius):
        self.radius = new_radius

# Circle class object created and print the area
my_circle = Circle(5)
print(my_circle.area()) # Result : 78.5
my_circle.set_radius(10)
print(my_circle.area()) # Result : 314.0

