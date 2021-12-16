n = {'total':[],'par':[],'impar':[]}
for x in range(1,21):
    n['total'].append(int(input('digite {}° numero: '.format(x))))
    if n['total'][-1] % 2 == 0:
        n['par'].append(n['total'][-1])
    else:
        n['impar'].append(n['total'][-1])
else:
    n['total'].sort()
    n['par'].sort()
    n['impar'].sort()
print('''
      todos os numeros:
      {}
      so os numeros pares:
      {}
      so os numeros impares:
      {}'''.format(n['total'],n['par'],n['impar']))