def greeting(name):
  print("Hello, " + name)
def add2(a,b):
    return(a+b)
def add3(a,b,c):
    return(a+b+c)
def square(a):
    return(a*a)
def area(r):
    return(3.1416*r*r)
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    return x / y
def modof(x,y):
    return(x%y)
def printtable(n):
    i = 1
    while i < 11:
        result=n*i
        print(str(n) + "X" + str(i) + "=" +str(result) )
        i += 1
def showList(lst):
    for x in lst:
        print(x,end=" "),
    print(" ")
def prime(n):
    i=2
    count=0
    while i<n:
        if(n%i==0):
           count+=1
        i+=1
    if count>0:
        print("This is Not Prime")
    else:
        print("This is Prime")