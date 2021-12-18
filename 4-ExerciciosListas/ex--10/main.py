import random

n = {'li':[1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80],'altura':[],'total':0}
for x in range(0,30):
    n['altura'].append(random.choice(n['li']))
    n['total'] += n['altura'][-1]
else:
    li = []
    num = n['total']/ 30
    for x in range(0,30):
        if n['altura'][x] <= num:
           li.append(n['altura'][x])        
    print('''
altura dos alunos: 
{}
media das alturas: 
{:.2f}
alturas abaixo da media: {}
{}'''.format(n['altura'],num,len(li),li))