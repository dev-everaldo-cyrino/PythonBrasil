g = 0.97
a = 0.96
op = int(input('''
1- gasolina R$2,50
2- alcool R$1,90
: '''))
litro = int(input('quantos litros: '))
if litro > 20:
    g = 0.95
    a = 0.94
if op == 1:
    total = 2.5 * g
    total = total * litro
    print('abasteceu {}.L de gasolina , total: R${:.2f}'.format(litro,total))
elif op == 2:
    total = 2.5 * a
    total = total * litro
    print('abasteceu {}.L de alcool , total: R${:.2f}'.format(litro,total))