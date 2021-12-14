salario = float(input('digite seu salario: '))
if salario > 0 and salario < 280:
    aumento = 1.2 * salario
    aumento1 = '20%'
elif salario >= 280 and salario < 700:
    aumento = 1.15 * salario
    aumento1 = '15%'
elif salario >= 700 and salario < 1500:
    aumento = 1.1 * salario
    aumento1 = '10%'
elif salario >= 1500:
    aumento = 1.05 * salario
    aumento1 = '5%'
print('''
o salário antes do reajuste; {}
o percentual de aumento aplicado; {}
o valor do aumento; {}
o novo salário, após o aumento; {}'''.format(salario,aumento1,aumento-salario,aumento))    