#Iter with Class
class MyNumbers:
  def __iter__(self):
    self.a = 1
    self.c = input("Enter Increment Value")
    return self
  def __next__(self):
    x = self.a
    self.a += int(self.c)
    return x

myclass = MyNumbers()
myiter = iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
