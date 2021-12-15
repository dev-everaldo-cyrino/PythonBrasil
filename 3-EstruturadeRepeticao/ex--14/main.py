n1=0
n2=0
n3=0
nulo = 0
print('''
      candidato1: 22
      candidato2: 37
      candidato3: 45''')

op = int(input('numero de eleitores: '))
for x in range(op):
    n = int(input('o voto da {}° pessoa vai para: '.format(x+1)))
    if n == 22:
        n1 +=1
    elif n == 45:
        n2+=1
    elif n == 37:
        n3 +=1
    else:
        nulo +=1
print('''
      nesta eleição tivemosos segintes votos
      candidato1: {}
      candidato2: {}
      candidato3: {}
      nulos: {}'''.format(n1,n2,n3,nulo))