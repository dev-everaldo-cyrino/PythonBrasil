print(' O programa deve ser encerrado quando não for informado o nome do atleta.')
while True:
    n = {'salto':[],'media':0}
    nome = input('nome do atleta: ')
    if nome == '':
        break
    for x in range(1,6):
        n['salto'].append(float(input('{}° salto: '.format(x))))
        n['media']+=n['salto'][-1]
    else:
        n['media']/=5
        print('''
Resultado final:
Atleta: {}
Saltos: {} m - {} m - {} m - {} m - {} m
Média dos saltos: {} m
-------------------------'''.format(nome,n['salto'][0],n['salto'][1],n['salto'][2]
                            ,n['salto'][3],n['salto'][4],n['media']))