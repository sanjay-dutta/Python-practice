# Class and object concept

class Robot:
    def introduce_self(self):
        print("My name is " + self.name)


r1 = Robot()
r1.name = "Tom"
r1.color = "Red"
r1.weight = 30
r1.introduce_self()

