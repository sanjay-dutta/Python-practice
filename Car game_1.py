#Car game_1

from distutils.cmd import Command
Command = ""
started = False
stopped = False
while True:
    Command = input("> ").lower()
    if Command == "start":
        if started:
            print("Car is already started! ")
        else:
            started = True
            print ("Car is started..")
    elif Command == "stop":
        if stopped: 
            print("Car is already stopped!")
        else:
            stopped = True 
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
