import re
txt = "Hello hai SrinivasaRao how are you"
x = re.search("^Hello.*ou$", txt)
print (x)
str = "Hello how are you"
#Check if the string starts with "Hello":
x = re.findall("\AHel", str)
print(x)
if (x):
  print("Yes, there is a match!")
else:
  print("No match")
str = "Hello how are you 5  students"
#Find all lower case characters alphabetically between "begin character" and "end character":
x = re.findall("[a-z,A-Z]", str)
print(x)
str = "Total Python Students is 50 members in 2020"
#Find all digit characters:
x = re.findall("\d", str) # find digits
print(x)
str = "Welcome to Python Students"
x = re.findall("W.l..m.", str)
print(x)
x = re.findall("P....n", str)
print(x)
