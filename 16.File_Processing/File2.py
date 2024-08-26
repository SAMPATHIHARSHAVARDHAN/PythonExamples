#if file is not existed then create a file(x)
# if file is existed then append the content
try:
    fname=input("Enter your file name")
    f = open(fname, "x")
    print("Enter content")
    f.write(input())
    f = open(fname, "r")
    print(f.read())
except:
     f = open(fname, "a")
     print("Enter Append Content")
     f.write("\n"+ input())
     f.close()
     f = open(fname, "r")
     print(f.read())
finally:
    f.close()