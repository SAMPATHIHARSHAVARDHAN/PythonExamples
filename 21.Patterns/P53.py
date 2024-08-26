"""
A B C D E F E F G H I
  A B C D E D E F G
    A B C D C D E
      A B C B C
        A B A
          A
"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
    print("  "*(i-1),end="")
    for j in range(1,num+2-i):
        print(chr(64+j),end=" ")
    for k in range(2,num+2-i):
        print(chr(68+k-i),end=" ")
    print()
