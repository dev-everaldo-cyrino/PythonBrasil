n = {0:1.2,1:1.3,2:1.5,3:1.2,4:1.3,5:1,'total':0}
print(n[4])
while True:
    num = int(input('''
Especificação   Código  Preço
Cachorro Quente 0     R$ 1,20
Bauru Simples   1     R$ 1,30
Bauru com ovo   2     R$ 1,50
Hambúrguer      3     R$ 1,20
Cheeseburguer   4     R$ 1,30
Refrigerante    5     R$ 1,00
: '''))
    if num >=0 and num <=5:
        quant = int(input('quantidade: '))
        n['total'] += n[num] * quant
        op = input('deseja encerrar(s/n): ')
        if op == 's':
            break
print('total: R$ ',n['total'])