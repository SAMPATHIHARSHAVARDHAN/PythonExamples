"""
A A A A A A
B B B B B
C C C C
D D D
E E
F
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(64+i),end=" ")
    print()
