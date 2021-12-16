n = {'aprovado':[],'nota7':[],'reprovado':[],'abaixo7':[],'total':0}
for x in range(1,11):
    print('-------------------------')
    aluno = input('nome do {}° aluno: '.format(x))
    n['total'] = 0
    for x in range(1,5):
        num = float(input('aluno {} ,{}° nota: '.format(aluno,x)))
        n['total'] += num
    else:
        n['total']/=4
        if n['total'] >=7:
            n['aprovado'].append(aluno)
            n['nota7'].append(n['total'])
        else:
            n['reprovado'].append(aluno)
            n['abaixo7'].append(n['total'])
print('''
      total aprovado: {}
      medias: {}
      alunos: {}
      
      total reprovado: {}
      medias: {}
      alunos: {}'''.format(len(n['aprovado']),n['nota7'],n['aprovado']
                    ,len(n['reprovado']),n['abaixo7'],n['reprovado']))