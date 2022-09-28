# Define person class
class Person:
    # initialize the instance
    def __init__(self, name):
        self.name = name


    def talk(self):
        print("talk")

        
# Object creation
Sanjay = Person("Sanjay Dutta")
print(Sanjay.name)
Sanjay.talk()