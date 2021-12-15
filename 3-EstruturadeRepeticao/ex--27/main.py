n = {'atleta':'','voto':[],'media':0}
while True:
    n['voto'] = []
    atleta = input('nome do atleta: ')
    n['atleta'] = atleta
    for x in range(1,8):
        voto = float(input('{}° voto: '.format(x)))
        n['voto'].append(voto)
    n['voto'].sort()
    n['media'] = (n['voto'][1]+n['voto'][2]+n['voto'][3]+n['voto'][4]+n['voto'][5])/5
    print('''
Melhor nota:  {} 
Pior nota: {} 
Média das demais notas: {:.2f} 
Resultado final:
{}: {:.2f} '''.format(n['voto'][-1],n['voto'][0],n['media'],n['atleta'],n['media']))