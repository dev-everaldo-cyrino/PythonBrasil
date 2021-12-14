n1 = int(input('primeiro numero: '))
n2 = int(input('segundo numero: '))
n3 = int(input('terceiro numero: '))

a = (2*n1) * (n2 / 2)
b = (3*n1) + n3
c = (n3*n3) * n3
print('''
o produto do dobro do primeiro com metade do segundo: {}
a soma do triplo do primeiro com o terceiro: {}
o terceiro elevado ao cubo: {} '''.format(a,b,c))