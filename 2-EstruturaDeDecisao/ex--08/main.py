hora = int(input('quantas horas trabalha por dia: '))
valor = float(input('valor da hora: '))
salario = hora * valor
if salario > 900 and salario <= 1500:
    ir = salario * 0.05
    irr = '5%'
elif salario > 1500 and salario <= 2500:
    ir = salario * 0.1
    irr = '10%'
elif salario > 2500:
    ir = salario * 0.2
    irr = '20%'
else:
    ir = 0
    irr = 'isento'
    
inss = salario * 0.1
fgts = salario * 0.11
total = ir+inss+fgts
print('''
Salário Bruto:           : R$ {:.2f}
(-) IR ({})            : R$ {:.2f}
(-) INSS ( 10%)          : R$ {:.2f}
FGTS (11%)               : R$ {:.2f}
Total de descontos       : R$ {:.2f}
Salário Liquido          : R$ {:.2f}'''.format(salario,irr,ir,inss,fgts,total,salario-total))