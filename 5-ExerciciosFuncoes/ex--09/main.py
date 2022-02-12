import random
num={'total':0,'pontos':0}
while True:
    n={'dado1':random.randint(1,6),'dado2':random.randint(1,6),'natural':[7,11],'craps':[2,3,12]}
    jogar = input('deseja jogar (s/n): ')
    if jogar == 'n':
        print('fim de jogo, seus pontos: {}\n'.format(num['pontos']))
        break
    else:
        print('dado1 = {}, dado2 ={}'.format(n['dado1'],n['dado2']))
        num['total']= n['dado1']+n['dado2']
        print('total: {}'.format(num['total']))
        if num['total']in n['natural']:
            print('um natural, vc ganhou\n')
            num['pontos']+=1
        elif num['total']in n['craps']:
            print('um craps , vc perdeu\n')
        else:
            print('um ponto , vc continua jogando\n')
            num['pontos']+=1