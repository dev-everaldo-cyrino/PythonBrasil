n1 = float(input('nota1 : '))
n2 = float(input('nota2 : '))
n3 = float(input('nota3 : '))
media = (n1+n2+n3) / 3
if media < 7:
    print('Reprovado !')
elif media >= 7 and media < 10:
    print('Aprovado')
elif media >= 10:
    print('Aprovado com Distinção')