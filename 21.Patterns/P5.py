"""
A B C D E
A B C D E
A B C D E
A B C D E
A B C D E
"""
n=int(input("Enter the number of rows: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(chr(64+j),end=" ")
    print()
