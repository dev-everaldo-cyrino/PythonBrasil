fatorial = int(input('digite um numero para o fatorial: '))
total = []
total1 = 1
for x in range(fatorial):
    total1 *= (x+1)
    total.append(fatorial-x)
print('{}! = {} = {}'.format(fatorial,total,total1))