fruits={"Apples","Grapes","FineApple"}
print(fruits)
for x in fruits:
  print(x,end=" "),
print("Apple" in fruits) # it returns true/false
x="Apples" in fruits
print(x)
if "Apples" in fruits:
  print("Yes Apples in Sets")
else:
  print("No Apples is not in sets")

fruits.add("Orange")
print(fruits)
fruits.update(["Orange","GreenApple","FineApple"])
print(fruits)
print(len(fruits))
fruits.remove("Orange")
fruits.pop()
#or
#fruits.discard("Orange")
print(fruits)
fruits.clear()
#or
#del fruits
print(fruits)


