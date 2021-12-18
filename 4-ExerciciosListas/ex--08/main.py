n =[]
total = 0
for x in range(1,11):
    n.append(int(input('digite o {}° numero: '.format(x))))
    print('{}^2 = {}'.format(n[-1],n[-1]**2))
    total += n[-1]**2
else:
    print('-------------------------------------------')
    print('a soma dos numeros elevado ao quadrado = ',total)