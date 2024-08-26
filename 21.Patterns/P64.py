"""
F
E F
D E F
C D E F
B C D E F
A B C D E F
B C D E F
C D E F
D E F
E F
F
"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(64+num-i+j),end=" ")
    print()
for a in range(1,num+1):
    for k in range(1,num-a+1):
        print(chr(64+k+a),end=" ")
    print()
