import random
n1 = []
n2 = []
n3 = []
for x in range(1,11):
    n1.append(random.randint(1,10))
    n2.append(random.randint(1,10))
else:
    for x in range(0,10):
        n3.append(n1[x])
        n3.append(n2[x])
print('''
      primeira lista:
      {}
      segunda lista:
      {}
      terceira lista:
      {}'''.format(n1,n2,n3))