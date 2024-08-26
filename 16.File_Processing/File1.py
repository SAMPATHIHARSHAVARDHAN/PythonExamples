#create new file and read created file
fname = input("Enter Your File Name")
f = open(fname, "w")
try:
    content=""
    print("Enter content (if you want exit press quit")
    while content!="quit":
        content=input()
        if content!="quit":
            f.write("\n"+content)
    f.close()

    f = open(fname, "r")
    print(f.read())

except:
    print("This File is already Existed. Please Give Other Name")
finally:
    f.close()