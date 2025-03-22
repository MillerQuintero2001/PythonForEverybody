# Name: Miller Quintero
# Date: Mar 11, 2025
# Brief: Example of classes in Python

class GenericObject:
    # Here we got the constructor
    def __init__(self, name):
        self.x = 0
        self.name = name
        print(f'The object {self.name} has been created')

    # Here we got a method
    def genericMethod(self):
        self.x = self.x + 1
        print(f'Generic Class {self.name} Value', self.x)

# To create the sub-class is important to pass the parent class as argument
class subGenericObject(GenericObject):
    # Here we got the constructor
    def __init__(self, name):
        # First, is necessary invoke the parent constructor
        super().__init__(name)
        # It is an alternative way to call the parent constructor
        GenericObject.__init__(self, name)
        # NOTE: If here we define the variable x, it will be overwritten from the parent class
        self.y = 0

    # Here we got a method
    def subGenericMethod(self):
        self.y = self.y + 7
        # Is not really necessary to call the parent method, but we can do it
        # super().genericMethod()
        print(f'Sub Generic Class {self.name} Value', self.y)

# Create the object
parent = GenericObject('Parent')
child = subGenericObject('Child')

# Call the methods
parent.genericMethod()
child.subGenericMethod()
child.subGenericMethod()
child.subGenericMethod()
child.genericMethod()
child.genericMethod()
child.subGenericMethod()
print(f'The X value of {child.name} class is {child.x}, and Y value is {child.y}')