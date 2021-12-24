so={'1':'Windows Server','2':'Unix','3':'Linux','4':'Netware','5':'Mac OS','6':'Outro'}
dados={'voto':0,'maiorx':'','maiory':0,'final':''}
contagem={'Windows Server':0,'Unix':0,'Linux':0,'Netware':0,'Mac OS':0,'Outro':0}
ordem={}
print('Qual o melhor Sistema Operacional para uso em servidores?')
print('''
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro''')
while True:
    num = input('opção: ')
    if int(num)>6:
        print('valor invalido, digite um valor entre 1-6 ou 0 para encerrar')
    elif num == '0':
        break
    else:
        contagem[so[str(num)]]+=50
        dados['voto']+=50
while True:
    dados['maiorx'] = ''
    dados['maiory'] = 0
    for x,y in contagem.items():    
        if y > dados['maiory']:
            dados['maiorx'] = x
            dados['maiory'] = y
    else:
        if dados['final']=='':
            dados['final']=dados['maiorx']
    if dados['maiory'] == 0:
        break
    else:
        ordem[dados['maiorx']] = dados['maiory']
        contagem.pop('{}'.format(dados['maiorx']))
print('''
Sistema Operacional             Votos         %
-------------------             -----         ---''')
for x,y in ordem.items():
    print('{:15}               {:5}           {:.1f}%'.format(x,y,(y/dados['voto'])*100))
else:
    print('''
-------------------             -----
Total                           {}

O Sistema Operacional mais votado foi o {}, com {} votos, correspondendo a {:.1f}%  dos votos.'''
.format(dados['voto'],dados['final'],ordem[dados['final']],(ordem[dados['final']]/dados['voto'])*100))