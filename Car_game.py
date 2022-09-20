#Car game:

from distutils.cmd import Command


Command = ""
while True:
    Command = input("> ").lower()
    if Command == "start":
        print("Car started...")
    elif Command == "stop":
        print("Car stopped...")
    elif Command == "help":
        print("""
start- to start the car
stop- to stopped the car
quit- to quit""")
    elif Command == "quit":
        break
    else:
        print("Sorry I don't understand that")







from distutils.cmd import Command


Command = ""
started = False
while True:
    Command = input("> ").lower()
    if Command == "start":
        if started:
            print("Car is already started! ")
        else:
            started = True
            print ("Car is started..")
    elif Command == "stop":
        if not started: 
            print("Car is already stopped")
        else:
            started = False
            print("Car is stopped...")
    elif Command == "help":
        print("""
start- to start the car
stop- to stopped the car
quit- to quit""")
    elif Command == "quit":
        break
    else:
        print("Sorry I don't understand that")
