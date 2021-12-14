pd = []
op = int(input('quantidade de produtos: '))
for x in range(op):
    pd.append(float(input('preço do {}° produto'.format(x+1))))
pd.sort()
print('''
o produto que vc deve comprar é o que custa R${}
e o que voce nunca deve comprar é o que custa R${}'''.format(pd[0],pd[-1]))