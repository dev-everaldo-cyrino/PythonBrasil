n = {'atleta':'','salto':[],'media':0}
while True:
    n['salto'] = []
    atleta = input('nome do atleta: ')
    n['atleta'] = atleta
    for x in range(1,6):
        salto = float(input('{}° salto: '.format(x)))
        n['salto'].append(salto)
    n['salto'].sort()
    n['media'] = (n['salto'][1]+n['salto'][2]+n['salto'][3])/3
    print('''
Melhor salto:  {} m
Pior salto: {} m
Média dos demais saltos: {:.2f} m

Resultado final:
{}: {:.2f} m'''.format(n['salto'][-1],n['salto'][0],n['media'],n['atleta'],n['media']))