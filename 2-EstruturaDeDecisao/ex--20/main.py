n1 = float(input('numero1: '))
n2 = float(input('numero2: '))
op = int(input('''
1- adição
2- multiplicação
3- subtração
4- divisão
:'''))
def num(n3):
    parimpa = n3 % 2
    if parimpa ==0:
        print('o numero é par')
    else:
        print('o numero é impar')
    sinal = n3
    if sinal > 0:
        print('o numero é positivo')
    else:
        print('o numero é negativo')
    deci = n3 - int(n3)
    if deci == 0:
        print('o numero é inteiro')
    else:
        print('o numero é decimal')
if op == 1:
    n3 = n1+n2
if op == 2:
    n3 = n1*n2
if op == 3:
    n3 = n1-n2
if op == 4:
    n3 = n1/n2
print('resultado ',n3)
num(n3)