n = int(input('Montar a tabuada de: '))
inicio = int(input('Começar por: '))
fim = int(input('Terminar em: '))
if fim < inicio:
    print('valores invalidos !')
else:
    for x in range(inicio , fim+1):
        print('{} x {} = {}'.format(n,x,x*n))