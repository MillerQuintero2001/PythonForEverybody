# Name: Miller Quintero
# Date: Mar 10, 2025
# Brief: Example of classes lifecycle

class Person:
    # Here we got the constructor
    def __init__(self, name = ''):
        self.age = 0
        self.name = name

    # Here we got a method that increments the age
    def setAge(self, age):
        self.age = age
        print(f'The age of {self.name} is {self.age}')
    
    # Here we got a method that deconstructs the object
    def __del__(self):
        print(f'The object {self.name} has been destroyed')

# Create some objects
p1 = Person('Miller')
p2 = Person('John')

p1.setAge(23)
# With this line we are destroying the object
p1 = 'dummy'

p2.setAge(25)
# With this other one we can also destroy the object, but it's 
# not necessary since the program will do it for us
# p2 = [1,5,9]