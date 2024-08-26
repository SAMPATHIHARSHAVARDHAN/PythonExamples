#thread with class sample program
from threading import *
class MyThread(Thread):
	def run(self):
		for i in range(10):
			print("\nChild Thread-" + str(i) )

t=MyThread()
t.start()
for i in range(10):
	print("\nMain Thread"+ str(i))
