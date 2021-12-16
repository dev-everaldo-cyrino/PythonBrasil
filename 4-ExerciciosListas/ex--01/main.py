import random
li = []
for x in range(1,11):
    li.append(random.randint(1,10))
li.sort()
for x in range(1,11):
    print(li[x])