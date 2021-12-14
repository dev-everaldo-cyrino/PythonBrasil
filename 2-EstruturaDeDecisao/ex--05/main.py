n1 = float(input('nota1: '))
n2 = float(input('nota2: '))
media = (n1 + n2) / 2
if media < 7:
    print('Reprovado, sua media é ',media)
elif media > 7 and media < 10:
    print('Aprovado, sua media é ',media)
elif media >= 10:
    print('Aprovado com Distinção, sua media é ',media)