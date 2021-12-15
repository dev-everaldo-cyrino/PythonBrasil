base = int(input('numero baae: '))
basefinal = base
n = int(input('expoente: '))
for x in range(n -1):
    basefinal *= base
print('o numero 2 ^ 3 = ',basefinal)