import platform

x = platform.system() # it returns Operating System Name
print(x)

x = dir(platform) # it shows the directory of platform
print(x)

for i in x:
    print(i)