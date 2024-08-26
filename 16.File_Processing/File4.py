import os
try:
  fname=input("Enter your filename ")
  f = open(fname, "r")
  print(f.read())
  f.close()

  f = open(fname, "r")
  print(f.read(5))
  f.close()

  f = open(fname, "r")
  print(f.readline())
  f.close()

  f = open(fname, "r")
  i=1
  for x in f:
    print(str(i) + x)
    i=i+1
  f.close()
  os.remove(fname)
except:
  print("Your Selected File is Not Existed")
