file = 5.8
alcatra = 6.8
picanha = 7.8
op = int(input('''
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
1- File Duplo      R$ 5,80 por Kg          R$ 4,90 por Kg 
2- Alcatra         R$ 6,80 por Kg          R$ 5,90 por Kg   
3- Picanha         R$ 7,80 por Kg          R$ 6,90 por Kg
:  '''))
kg = int(input('quantos kilos: '))
if kg >5:
    file = 4.9
    alcatra = 5.9
    picanha = 6.9
if op == 1:
    print('total: R${:.2f}'.format(kg *file))
elif op == 2:
    print('total: R${:.2f}'.format(kg *alcatra))
elif op == 3:
    print('total: R${:.2f}'.format(kg *picanha))