tintag = 0
tintap = 0
tintamg = 0
tintamp = 0
area = float(input('digite a area a ser pintada: '))
area /= 6
area1 = area
while area1 > 0:
    area1 -= 18
    tintag +=1
    
area1 = area    
while area1 > 0: 
    area1 -= 3.6
    tintap += 1

area1 = area
while area1 > 14.4:
    area1 -=18
    tintamg +=1
print(area1)

while area1 > 0:
    area1 -= 3.6
    tintamp += 1

print('''
comprar apenas latas de 18 litros; {}.galões e R${}
comprar apenas galões de 3,6 litros; {}.litros e R${}
misturar latas e galões : {}.galoes e {}.litros total R${}'''.format(tintag,tintag*80,tintap,tintap*25,tintamg,tintamp,tintamg*80 + tintamp*25  ))