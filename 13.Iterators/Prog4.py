class MyNumbers:
  def __init__(self,start):
    self.x=start
  def __iter__(self):
    self.a = x
    return self
  def __next__(self):
    if self.a <= 100:
      x = self.a
      self.a += 10
      return x
    else:
      raise StopIteration

x=int(input("Enter Start value"))
myclass = MyNumbers(x)
myiter = iter(myclass)
for x in myiter:
  print(x)