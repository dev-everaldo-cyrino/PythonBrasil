import random
n={1:0,2:0,3:0,4:0,5:0,6:0}
for x in range (1,101):
    num = random.randint(1,6)
    n[num]+=1
    print('processando dados {}%'.format(x))
else:
    print('''
          ''')
    for x,y in n.items():
        print('valor:{}  -  {}'.format(x,y))