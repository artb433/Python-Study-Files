import random

numList = []
for i in range(5):
    numList.append(random.randrange(1, 9))
numList.insert(5, 10)
numList.remove(10)
numList.pop(1)

print(numList)
for i in numList:
    print(i)
