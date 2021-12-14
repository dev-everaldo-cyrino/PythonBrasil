num = input('digite um numero de 1 a 1000: ')
if int(num)> 0 and int(num) < 1000:
    n = len(num)
    if n == 1:
        print('{} = {} unidades'.format(num,num))
    elif n == 2:
        print('{} = {} dezenas  e  {} unidades'.format(num,num[0],num[1]))
    elif n == 3:
        print('{} = {} centenas  ,  {} dezenas  e  {} unidades'.format(num,num[0],num[1],num[2]))
else:
    print('numero invalido')