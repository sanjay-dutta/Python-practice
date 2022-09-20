numbers = [0, 5, 8, 3, 7, 2, 9]
max = numbers[0] # assuming the first number as max
for number in numbers:
    if number > max:
        max = number
print(max)