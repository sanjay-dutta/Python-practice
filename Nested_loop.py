#Nested loops:

 # the inner loops complete after 3 iterations, and then it goes out to the main loops.

for x in range(4):
	for y in range(3): 
		print(x, y)


for x in range(4):
	for y in range(3):
		print(f'({x}, {y})')
for x in range(4):
	for y in range(3):
		print((x, y))

numbers = [5, 2, 5, 2]
for x in numbers:
    output = ''
    for count in range (x):
        output += 'x'
    print (output)
