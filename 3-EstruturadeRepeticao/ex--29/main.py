n = int(input('digite um numero: '))
n1=1
n2=1
total=1
num = ['1/1']
while n1 < n:
    n1 += 1
    n2 += 2
    num.append('+ {}/{}'.format(n1,n2))
    total += n1/n2
print('''
a sequencia de numeros é
{}
e sua soma é = {:.4f}'''.format(num,total))