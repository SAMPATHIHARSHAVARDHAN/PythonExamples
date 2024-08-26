#before removing the file check the file is existed or not
import os
filename=input("Enter your file name")
if os.path.exists(filename):
  os.remove(filename)
  print ("File Success fully Deleted")
else:
  print("The file does not exist")

