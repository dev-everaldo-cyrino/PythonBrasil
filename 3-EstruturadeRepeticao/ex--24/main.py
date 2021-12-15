n = {1:0,2:0,3:0,4:0,'nulo':0,'branco':0}
while True:
    op = int(input('''
------faça seu voto------
1 - Jose
2 - Pedro
3 - Antoinho
4 - Adelson
5 - Voto Nulo
6 - Voto em Branco
: '''))
    if op == 0:
        break
    elif op ==1:
        n[1] +=1
    elif op ==2:
        n[2] +=1
    elif op ==3:
        n[3] +=1
    elif op ==4:
        n[4] +=1
    elif op ==5:
        n['nulo'] +=1
    elif op ==6:
        n['branco'] +=1
print('------------------------')
for x,y in n.items():
    print('{} = {}'.format(x,y))