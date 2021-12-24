n={'carro':0,'nome':[],'km':[],'maiseconomico':'','kmeconomico':0}
print('encerre o programa colocando 0 no nome')
while True:
    print('')
    n['carro']+=1
    print('veiculo {}'.format(n['carro']))
    nome= input('nome: ')
    if nome == '0':
        break
    n['nome'].append(nome)
    n['km'].append( float(input('Km por litro: ')))
    if n['km'][-1]>n['kmeconomico']:
        n['kmeconomico']=n['km'][-1]
        n['maiseconomico']=n['nome'][-1]
print('''

Relatório Final''')
for x in range(0,len(n['km'])):
    valor = 1000/n['km'][x]
    print('{:2} - {:8}           -    {:4.1f} -  {:5.1f} litros - R$ {:5.2f}'
          .format(x+1,n['nome'][x],n['km'][x],valor,valor*2.25))
else:
    print('O menor consumo é do {}.'.format(n['maiseconomico']))