"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=" ")
    print()
