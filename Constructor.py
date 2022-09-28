"""
Python is an object-oriented programming language.
Almost everything in Python is an object, with its properties and methods.
A Class is like an object constructor or a "blueprint" for creating objects.
Syntax: Class Definition 
class ClassName:
    # Statement
"""
"""
Constructors are generally used for instantiating an object. 
The task of constructors is to initialize(assign values) to the data members of the class when an object of the class is created. 
In Python the __init__() method is called the constructor and is always called when an object is created.

Syntax of constructor declaration : 
def __init__(self):
    # body of the constructor


Types of constructors : 
default constructor: The default constructor is a simple constructor which doesn’t accept any arguments. 
Its definition has only one argument which is a reference to the instance being constructed.

parameterized constructor: constructor with parameters is known as parameterized constructor. 
The parameterized constructor takes its first argument as a reference to the instance being constructed known as self and the rest of the arguments are provided by the programmer.

"""
class GeekforGeeks:

	# default constructor
	def __init__(self):
		self.geek = "GeekforGeeks"

	# a method for printing data members
	def print_Geek(self):
		print(self.geek)


# creating object of the class
obj = GeekforGeeks()

# calling the instance method using the object obj
obj.print_Geek()
