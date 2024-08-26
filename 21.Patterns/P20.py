"""
6 5 4 3 2 1
6 5 4 3 2
6 5 4 3
6 5 4
6 5
6
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(n+1-j,end=" ")
    print()
