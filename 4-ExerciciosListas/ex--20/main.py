n= {'1':0,'2':0,'3':0,'4':0,'total':0}
print(' identificação igual a zero encerra o programa')
print('''
1- necessita da esfera        
2- necessita de limpeza     
3- necessita troca do cabo ou conector
4- quebrado ou inutilizado
''')
while True:
    op = input('opção: ')
    if op == '0':
        break
    else:
        quant = int(input('quantidade: '))
        n[op]+=quant
        n['total']+=quant
print('''
Quantidade de mouses: {}'''.format(n['total']))
print('''
Situação                           Quantidade              Percentual
1- necessita da esfera                  {:3}                   {:.0f}%
2- necessita de limpeza                 {:3}                   {:.0f}%
3- necessita troca do cabo ou conector  {:3}                   {:.0f}%
4- quebrado ou inutilizado              {:3}                   {:.0f}%
'''.format(n['1'],(n['1']/n['total'])*100,n['2'],(n['2']/n['total'])*100,
           n['3'],(n['3']/n['total'])*100,n['4'],(n['4']/n['total'])*100))