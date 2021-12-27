n = {'total':0,'quant':0}
def pagar(d,a):
    if a == 0:
        print('0 de juros. valor pago = {}\n'.format(d))
    else:
        total = ((a*0.001)+0.03+1)*d
        n['total']+=total
        n['quant']+=1
        print('''
3%  de juros + {}%  dos dias. valor pago = {:.2f} \n'''.format(a*0.1,total))
while True:
    divida = float(input('valor da parcela: '))
    if divida == 0:
        print('foram pagas {} parcelas hj. total = {}\n'.format(n['quant'],n['total']))
        break
    atraso = int(input('dias de atraso: '))
    pagar(divida,atraso)
    