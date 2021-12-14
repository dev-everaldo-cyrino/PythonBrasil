semana = ['domingo','segunda','terça','quarta','quinta','sexta','sabado']
dia = int(input('digite um numero de 1-7: '))
if dia <= 0 or dia > 7:
    print('numero invalido !')
else:
    print('o dia de hoje é {}'.format(semana[dia-1]))