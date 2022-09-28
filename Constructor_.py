class Person:
    def __init__(self, name):
        self.name = name


    def talk(self):
        print("talk")

Sanjay = Person("Sanjay Dutta")
print(Sanjay.name)
Sanjay.talk()