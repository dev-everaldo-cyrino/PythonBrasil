peixe = float(input('quantos kilos de peixe vai enviar: '))
if peixe > 50:
    multa = peixe - 50
    multa *= 4
    print('a multa é de R${:.2f}'.format(multa))
else:
    print('apenas {:.0f}kg enviado, sem multas hj'.format(peixe))