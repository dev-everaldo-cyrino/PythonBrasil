n=''
num = input('digite um numero inteiro: ')
for x in range(1,len(num)+1):
    n = n + n.join(num[-x])
print(n)