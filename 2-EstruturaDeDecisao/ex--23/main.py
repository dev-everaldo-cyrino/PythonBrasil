op = int(input('''
                      Até 5 Kg           Acima de 5 Kg
1- Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
2- Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
: '''))
if op == 1:
    op = 2.5
else:
    op = 1.8
kg = int(input('quantos kilos: '))
if kg > 5:
    op *= 0.88
    op *= kg
else:
    print('total: R${:.2f}'.format(op*kg)) 
if kg > 8:
    op *= 0.9
    print('total: R${:.2f}'.format(op))