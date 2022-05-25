# convert weights 
weight = float (input("weight: "))
unit = input ("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbd: " + str(converted))
else:
    converted = weight * 0.45
    print ("weight in kgs :" + str(converted))