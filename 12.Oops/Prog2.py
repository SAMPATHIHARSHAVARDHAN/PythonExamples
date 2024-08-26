#assign values dirctly in class memebers
class MyClass:
    def __init__(self,code,name):
       self.code=code
       self.name=name
    def showData(self):
       print(self.code)
       print(self.name)
p=MyClass(100,"SrinivasaRao")
p.showData()
p.code=input("Enter Code")
p.name=input("Enter Name")
p.showData()
print("Code:"+ p.code)
print("Name:" + p.name)