"""
F
F E
F E D
F E D C
F E D C B
F E D C B A
F E D C B
F E D C
F E D
F E
F
"""
num=int(input("Enter a number:"))
for i in range(1,num+1):
    for j in range(1,i+1):
        print(chr(65+num-j),end=" ")
    print()
for a in range(1,num+1):
    for k in range(num-a,0,-1):
        print(chr(64+k+a),end=" ")
    print()

