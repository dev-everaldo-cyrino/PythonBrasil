n = []
par = 0
impar = 0
for x in range(10):
    n.append(int(input('{}° numero: '.format(x+1))))
for x in range(len(n)):
    if n[x] % 2 == 0:
        par +=1
    else:
        impar +=1
print('par = ',par)
print('impar = ',impar)