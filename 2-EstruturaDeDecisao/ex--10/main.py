n1 = float(input('nota1: '))
n2 = float(input('nota2: '))
media = (n1+n2) / 2

if media > 9 and media <=10:
    conceito = 'A'
    res = 'aprovado'
elif media > 7.5 and media <= 9:
    conceito = 'B'
    res = 'aprovado'
elif media > 6 and media <= 7.5:
    conceito = 'C'
    res = 'aprovado'
elif media > 4 and media <= 6:
    conceito = 'D'
    res = 'reprovado'
elif media >= 0 and media <= 4:
    conceito = 'E'
    res = 'reprovado'
else:
    conceito = ' -invalido- '
    res = ' -invalido- '
    
print('''
nota 1   : {}
nota 2   : {}
media    : {}
conceito : {}
resultado: {}'''.format(n1,n2,media,conceito,res))