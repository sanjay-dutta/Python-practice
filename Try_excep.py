#The try block lets you test a block of code for errors.
#The except block lets you handle the error.
try: 
    age = int(input("age: "))
    print(age)
except ValueError:
    print("Invalid value")