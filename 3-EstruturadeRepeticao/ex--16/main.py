x = 1
total = 0
while True:
    n = float(input('Produto {}: R$ '.format(x)))
    x += 1
    total += n
    if n == 0:
        break
print('Total: R$ ',total)
troco = float(input('dinheiro: R$ '))
print('Troco: R$ {}'.format(troco - total))