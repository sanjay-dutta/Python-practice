# Create a list and add number 12 to the list
numbers = [5, 2, 1, 7, 4]
numbers.append(12)
print(numbers)

numbers = [5, 2, 1, 7, 4]
# Insert 14 in the begining of the list in the index 0
numbers.insert(0, 14) 
print(numbers)

numbers = [5, 2, 1, 7, 4]
# Remove 5 from the list
numbers.remove(5)
print(numbers)

# Clear the items from the list
numbers = [5, 2, 1, 7, 4]
numbers.clear()
print(numbers)

# Remove the last item in the list
numbers = [5, 2, 1, 7, 4]
numbers.pop()
print(numbers)

# Index method
numbers = [5, 2, 1, 7, 4]
# print(numbers.index(3))
print(numbers.index(5))
# sort items in assending order
numbers.sort()
print(numbers)

# Reverse the string
numbers = [5, 2, 1, 7, 4]
numbers.sort()
numbers.reverse()
print(numbers)

# Copy a list
numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
numbers.append(19)
print(numbers)
print(numbers2)

# Write a program to remove the duplicatea in a list
numbers = [2, 2 , 4, 6, 3, 4, 4, 1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

