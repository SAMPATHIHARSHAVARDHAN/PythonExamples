strcmd = ""
started = False
while strcmd != "quit":
    strcmd = input("Enter Command(Start,Stop,Quit)").lower()
    if strcmd == "start":
        if started == True:
            print("Game is Alerady Started")
        else:
            started = True
            print("Game is Starts")
    elif strcmd == "stop":
        if started == False:
            print("Game Not Started")
        else:
            started = False
            print("Stop the Game")
    elif strcmd == "quit":
        print("Your Game is Quit")
        break
    elif strcmd != "start" or strcmd != "stop" or strcmd != "quit":
        print("Your Given Command Not in list(Start,Stop,Quit) ")
