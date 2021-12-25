n = {}
num = {'total':0,'contador':0}
print('espaço igual a zero encerra.')
while True:
    user = input('usuario: ')
    espaço = int(input('espaço usado em Kb: '))
    if espaço == 0:
        break
    else:
        n[user]=espaço
        num['total'] +=espaço
print('''
ACME Inc.               Uso do espaço em disco pelos usuários
------------------------------------------------------------------------
Nr.  Usuário          Espaço utilizado          %  do uso
''')
num['total']/=1024
num['total']/=1024
for x,y in n.items():
    num['contador']+=1
    print('{:3}   {:11}     {:8.2f} MB      {:.2f}%'
.format(num['contador'],x , (y/1024)/1024, (((y/1024)/1024)/num['total'])*100))
else:
    print('''
Espaço total ocupado: {:.2f} MB
Espaço médio ocupado: {:.2f} MB'''.format(num['total'],num['total']/len(n)))