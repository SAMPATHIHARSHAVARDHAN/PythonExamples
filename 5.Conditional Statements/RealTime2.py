strcmd = ""
Flag = 0
while strcmd != "quit":
    strcmd = input("Enter Command(Start,Stop,Quit)").lower()
    if strcmd == "start":
        if Flag == 1:
            print("Game is Alerady Started")
        else:
            Flag = 1
            print("Game is Starts")
    elif strcmd == "stop":
        if Flag == 0:
            print("Game Not Started")
        else:
            Flag = 0
            print("Stop the Game")
    elif strcmd == "quit":
        print("Your Game is Quit")
        break;
    elif strcmd != "start" or strcmd != "stop" or strcmd != "quit":
        print("Your Given Command Not not list(Start,Stop,Quit) ")
