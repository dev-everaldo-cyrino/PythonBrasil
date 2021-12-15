num = {'0-25':0,'26-50':0,'51-75':0,'76-100':0}
while True:
    n= int(input('digite um numero: '))
    if n < 0:
        print('numero negativo')
    elif n >=0 and n<=25:
        print('esta no intervalo de 0-25')
        num['0-25'] +=1
    elif n >=26 and n<=50:
        print('esta no intervalo de 26-50')
        num['26-50'] +=1
    elif n >=51 and n<=75:
        print('esta no intervalo de 51-75')
        num['51-75'] +=1
    elif n >=76 and n<=100:
        print('esta no intervalo de 76-100')
        num['76-100'] +=1
    else:
        print('numero superior a 100')
    for x,y in num.items():
        print('{} = {}'.format(x,y))