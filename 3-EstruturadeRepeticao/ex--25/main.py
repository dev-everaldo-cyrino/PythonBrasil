gabarito = {1:'A',2:'B',3:'C',4:'D',5:'E',6:'E',7:'D',8:'C',9:'B',10:'A'}
n = {'mn':[],'alunos':0,'total':0,'totalalone':0}
for x in range(1,11):
    gab = input('Resposta da questão {}: '.format(x))
    gabarito[x] = gab
while True:
    n['totalalone'] = 0
    op = int(input('precione 0 para sair: '))
    if op == 0:
        break
    n['alunos'] +=1
    for x in range(1,11):
        nota = input('nota {}: '.format(x))
        if nota.upper() == gabarito[x]:
            n['totalalone'] +=1
            n['total'] +=1
        if x == 10:
            n['mn'].append(n['totalalone'])
n['mn'].sort()
print('''
total de aluno: {}
maior nota:     {}
menor nota:     {}
media da turma: {}'''.format(n['alunos'],n['mn'][0],n['mn'][-1],n['total']/n['alunos']))