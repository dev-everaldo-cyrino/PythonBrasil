n = {'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0,'10':0,'11':0,'12':0,
    '13':0,'14':0,'15':0,'16':0,'17':0,'18':0,'19':0,'20':0,'21':0,'22':0,'23':0,}
li = {}
variavel = {'voto':0,'total':0,'numero':'','melhor jogador':''}
while True:
    num = input('digite o numero do voto: ')
    if int(num)>23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    elif num == '0':
        break
    else:
        n[num]+=1
        variavel['voto']+=1
        
while True:
    variavel['total']=0
    variavel['numero']=''
    for x,y in n.items():
        if y > variavel['total']:
            variavel['total']=y
            variavel['numero'] = x
    if variavel['total'] == 0:
        break
    else:
        if variavel['melhor jogador']=='':
            variavel['melhor jogador']= variavel['numero']
        li[variavel['numero']]=variavel['total']  
        n.pop('{}'.format(variavel['numero']))
    
print('''
Resultado da votação:

Foram computados {} votos.

Jogador         Votos               %
'''
.format(variavel['voto']))
for x,y in li.items():
    print('{:2}              {:2}               {:.1f}%'.format(x,y,(y/variavel['voto'])*100))
else:
    print('O melhor jogador foi o número {}, com {} votos, correspondendo a {:.1f}%  do total de votos.'
.format(variavel['melhor jogador'],li[variavel['melhor jogador']],(li[variavel['melhor jogador']]/variavel['voto'])*100))
            
    