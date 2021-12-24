n = {'menorque100':0,'maiorabono':0,'totaldeabono':0,'salario':[],'abono':[]}
print('''valor 0 encerra a operação.

Projeção de Gastos com Abono
============================ ''')
while True:
    num = float(input('salario: '))
    if num ==0:
        break
    else:
        n['salario'].append(num)
        abono = n['salario'][-1] * 0.2
        if abono <=100:
            abono = 100
            n['abono'].append(abono)
            n['menorque100']+=1
            n['totaldeabono']+=abono
        else:
            n['abono'].append(abono)
            n['totaldeabono']+=abono
            if abono > n['maiorabono']:
                n['maiorabono']=abono
print('''

Salário    - Abono     ''')
for x in range(0,len(n['salario'])):
    print('R$ {:5.2f} - R$  {:5.2f}'.format(n['salario'][x],n['abono'][x]))


print('''
Foram processados {} colaboradores
Total gasto com abonos: R$ {:.2f}
Valor mínimo pago a {} colaboradores
Maior valor de abono pago: R$ {:.2f}'''.format(len(n['salario']),n['totaldeabono'],
                                        n['menorque100'],n['maiorabono']))