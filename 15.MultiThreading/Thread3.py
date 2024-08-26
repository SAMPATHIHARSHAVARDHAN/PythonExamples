from threading import *
#from threading import *
class Test:
    def display(self):
        for i in range(10):
            print("\nChild Thread-2 " + str(i))
obj=Test()
t=Thread(target=obj.display)
t.start()
for i in range(11):
    print("Main Thread-2 " + str(i))

