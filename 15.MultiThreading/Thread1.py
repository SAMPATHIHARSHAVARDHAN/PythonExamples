from threading import *
def display():
    for i in range(1,11):
        print("\nYour inside of Thread " + str(i))

t=Thread(target=display) #creating Thread object
t.start() #starting of Thread

for i in range(1,11):
    print("\nYou are in main program" + str(i))
