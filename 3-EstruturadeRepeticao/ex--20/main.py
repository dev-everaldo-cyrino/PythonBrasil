dc = {'alto':0,'baixo':3,'nome1':'','nome2':''}
for x in range(10):
    nome = input('nome da {}° pessoa: '.format(x+1))
    altura = float(input('altura em cm da pessoa: '))
    print('------------------------------------')
    if altura < dc['baixo']:
        dc['baixo'] = altura
        dc['nome1'] = nome
    if altura > dc['alto']:
        dc['alto'] = altura
        dc['nome2'] = nome
print('''
      o mais alto é {} com {} cm
      o mais baixo é {} com {} cm'''.format(dc['nome2'],dc['alto'],dc['nome1'],dc['baixo']))