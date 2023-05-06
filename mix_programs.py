# Using Variables in Strings
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# use f-strings to compose complete messages
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}")

# To add a newline in a string, use the character combination \n:
#print("Languages:\nPython\nC\nJavaScript") 
message = "The greatest glory in living lies not in never falling, but in rising every time we fall."
famous_person = "Nelson Mandela"
print(f'"{message}" - {famous_person}')
num1 = input("Enter a number: ") 

num2 = input("Enter another number: ") 

result = float(num1) + float(num2) 

print("Result is: " + str(result)) 

name = input("Enter your name: ")
age = input("Enter your age: ")
address = input("Enter your address: ")
print("My name is " + name)
print("My age is " + age)
print("My address is " + address)

friends = ["Sanjay", "Morami", "Lalit", "Diganta", "Tanmoy"]
age = [33, 34, 23, 67, 45, 34]
friends.extend(age)
friends.insert(2, "udh")
print(friends.index("uu"))

coordinate = (2, 5)
print(coordinate)

def sayhi():
    print("Hi Dip")


sayhi() # calling the function

def sayhi(name):
    print("Hello you are")

print("top")
sayhi() # calling the function
print("Bottom")

def sayhi(name, age): # name and age are parameters here
    print("Hello " + name + ", you are " + age)


sayhi("Sanjay", "30")


def cube(num):
    return(num*num*num)


print(cube(4))

def cube(num):
    print("code")
    return(num*num*num)
    

result = cube(4)
print(result)


is_male = True

if is_male:
    print("You are a male")
    

is_male = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

    

is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neithe male nor tall")



is_male = False
is_tall = False

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neithe male nor tall")

    is_male = True
is_tall = False

if is_male and is_tall:
    print("You are a male or tall or both")
else:
    print("You are neithe male nor tall")


is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but tall")
else:
    print("You are neithe male nor tall")

# If Statements & Comparisons
def max_num(num1, num2, num3):
    if num1>num2 and num1>num3:
        return(num1)
    elif num2>num1 and num2>num3:
        return(num2)
    else:
        return(num3)  


print(max_num(3, 4, 5))


#Building a better Calculator

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
op = input("Enter the operator: ")


if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid operator")


# Dictionaries
days_in_months = {
    "january":31,
    "february":28,
    "march":31,
    "april":30,
    "may":31,
    "june":30,
    "july":31,
    "august":31,
    "september":30,
    "october":31,
    "november":30,
    "december":31
}

m = input("Enter name of month: ")
print(days_in_months[m])    

# while loop
i = 1 
while i <= 10:
    print(i)
    i += 1
    

print("Done with loop")


# Building a Guessing Game
secret_word = "giraffe"
guess = ""
while guess != secret_word:
    guess = input("Enter guess: ")


print("You win!")


# Building a Guessing Game1
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses: 
    print("Out of guesses, YOU LOSE!")
else:
    print("YOU WON!")


# For Loops
for Letter in "Giraffe Academy":
    print(Letter)


friends = ["Sanjay", "Archi", "Lalit", "Sarah"]
for name in friends:
    print(name)

for index in range(5):
    if index == 0:
        print("First iteration")
    else: 
        print("Not first")


# Exponent function
def raise_to_power(base_num, pow_num):
    result = 2   
    for index in range(pow_num):
        result = result * base_num
    return(result)

print(raise_to_power(3, 2))


# 2D Lists & Nested Loops

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]


print(number_grid[0][0])

number_grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]


for row in number_grid:
    for col in row:
        print(col)


# Build a Translator
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "g"
        else:
            translation = translation + letter 
    return(translation)


print(translate(input("Enter a phrase: ")))

# Try / Except
try:
    number = int(input("Enter a number"))
    print(number)
except:
    print("Invalid Input")

# Reading Files

employee_file = open("employees.txt", "r+")
print(employee_file.read())
employee_file.close()
# Reading Files - Reading Lines
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()
    """



