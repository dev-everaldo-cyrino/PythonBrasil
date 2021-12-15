a = int(input('primeiro numero: '))
b = int(input('segundo numero: '))
total = 0
alista = []
while a != b-1:
    a +=1
    total += a
    alista.append(a)
print('''
      entre o numero {} e {}
      temos os numeros {}
      e a soma desse numeros é = {}'''.format(alista[0]-1,b,alista,total))