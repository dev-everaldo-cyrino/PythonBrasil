n = int(input('digite um numero: '))
n2=1
total=1
num = ['1/1']
while n2 < n:
    n2 += 1
    num.append('+ 1/{}'.format(n2))
    total += 1/n2
print('''
a sequencia de numeros é
{}
e sua soma é = {:.6f}'''.format(num,total))