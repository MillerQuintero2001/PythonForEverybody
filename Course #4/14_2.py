# Name: Miller Quintero
# Date: Mar 10, 2025
# Brief: Example of classes in Python

class GenericObject:
    # Here we got the constructor
    def __init__(self):
        self.x = 0

    # Here we got a method
    def genericMethod(self):
        self.x = self.x + 1
        print('Generic Class Value', self.x)

# Create the object
varObject = GenericObject()

# Call the method
varObject.genericMethod()
varObject.genericMethod()
varObject.genericMethod()
# Another way to call the method
GenericObject.genericMethod(varObject)
GenericObject.genericMethod(varObject)

print(type(varObject))
print(type(varObject.x))
print(type(GenericObject))
print(type(GenericObject()))
print(type(GenericObject.genericMethod))
print(type(GenericObject.genericMethod(varObject)))
print(dir(varObject))
print(type(varObject.genericMethod))

