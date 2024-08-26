strcmd = ""
Flag = "Off"
while strcmd != "quit":
    strcmd = input("Enter Command(Start,Stop,Quit)").lower()
    if strcmd == "start":
        if Flag == "On":
            print("Game is Alerady Started")
        else:
            Flag = "On"
            print("Game is Starts")
    elif strcmd == "stop":
        if Flag == "Off":
            print("Game Not Started")
        else:
            Flag = "Off"
            print("Stop the Game")
    elif strcmd == "quit":
        print("Your Game is Quit")
        break;
    elif strcmd != "start" or strcmd != "stop" or strcmd != "quit":
        print("Your Given Command Not not list(Start,Stop,Quit) ")
