"""
A
B B
C C C
D D D D
E E E E E
F F F F F F
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(chr(64+i),end=" ")
    print()
