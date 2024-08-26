"""
F E D C B A
F E D C B
F E D C
F E D
F E
F
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print(chr(65+n-j),end=" ")
    print()
