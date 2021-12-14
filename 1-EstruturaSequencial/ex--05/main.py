hora = int(input('quantas horas trabalha por mes: '))
money = float(input('quanto ganha por hora: '))
salario = hora * money
ir = salario * 0.11
inss = salario * 0.08
sindicato = salario * 0.05
salario2 = (((salario - ir)-inss)-sindicato)
print('''
+ Salário Bruto : R${}
- IR (11%) : R${}
- INSS (8%) : R${}
- Sindicato ( 5%) : R${}
= Salário Liquido : R${}'''.format(salario,ir,inss,sindicato,salario2))