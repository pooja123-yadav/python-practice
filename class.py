
class Dog:

    # class attribute
    attr1 = "mammal"
    
    # Instance attribute
    # It is run as soon as an object of a class is instantiated. The method is useful to do any initialization you want to do with your object.
    def __init__(self, name):
    	self.name = name

    def speak(self):
        print("My name is {}".format(self.name))

# Driver code
# Object instantiation
Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

Rodger = Dog("Rodger")
Tommy = Dog("Tommy")

# Accessing class attributes
print("Rodger is a {}".format(Rodger.__class__.attr1))
print("Tommy is also a {}".format(Tommy.__class__.attr1))

# Accessing instance attributes
print("My name is {}".format(Rodger.name))
print("My name is {}".format(Tommy.name))

# Accessing class methods
Rodger.speak()
Tommy.speak()
