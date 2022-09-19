#If statement

is_hot = True
if is_hot:
	print ("It's a hot day")
print ('Enjoy your day')

is_hot = False
if is_hot:
	print ("It's a hot day")
print ('Enjoy your day')

is_hot = False
if is_hot:
	print ("It's a hot day")
	print ('Enjoy your day')

is_hot = True
if is_hot:
	print ("It's a hot day")
	print ('Drink planty of water')
else:
	print ("It's a cold day")
	print ("Wear warm cloths")
print ("Enjoy your day")


is_hot = True
if is_hot:
	print ("It's a hot day")
	print ('Drink planty of water')
else:
	print ("It's a cold day")
	print ("Wear warm cloths")
print ("Enjoy your day")



is_hot = False
is_cold = True
if is_hot:
	print ("It's a hot day")
	print ('Drink planty of water')
elif is_cold:
	print ("It's a cold day")
	print ("Wear warm cloths")
else:
	print ("It's a lovely day")
print ("Enjoy your day")


is_hot = False
is_cold = False
if is_hot:
	print ("It's a hot day")
	print ('Drink plenty of water')
elif is_cold:
	print ("It's a cold day")
	print ("Wear warm cloths")
else:
	print ("It's a lovely day")
print ("Enjoy your day")


price = 100000
good_credit = True

if good_credit:
	print (0.1 * 100000)
	
else:
	print (0.2 * 100000)
