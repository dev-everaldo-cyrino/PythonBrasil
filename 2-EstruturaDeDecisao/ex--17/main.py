n = int(input('valor do saque: '))
num = n
nota1 = 0
nota5 = 0
nota10 = 0
nota50 = 0
nota100 = 0

while n > 1:
    if n >=100:
        n -=100 
        nota100 +=1
    elif n >= 50:
        n -=50
        nota50 +=1
    elif n >=10:
        n -=10
        nota10 +=1
    elif n >=5:
        n -=5
        nota5 +=1
    elif n >=1:
        n -=1
        nota1 +=1
print('''
valor do saque = {}
foram emitidas notas de:
{} de R$100
{} de R$50
{} de R$10
{} de R$5
{} de R$1'''.format(num,nota100,nota50,nota10,nota5,nota1))