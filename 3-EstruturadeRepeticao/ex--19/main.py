taxa = 1.015
n = float(input('salario: '))
n1 = n
for x in range(1997,2022):
    print('no ano de {} o salario foi de {:.2f} para {:.2f}'.format(x,n1,n*taxa))
    n1 = n * taxa
    taxa *= 1.015