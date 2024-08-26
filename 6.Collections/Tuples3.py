import random
flower_name=("Red Rose","Green Rose","Rose","Yello Rose","White Rose","Orange Rose")
n=int(input("Tell Any One Number between 0...6"))
n=random.randrange(0,n)
print(flower_name[n])