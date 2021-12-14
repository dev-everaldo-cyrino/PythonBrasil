tinta = 0
area = float(input('area em metros quadradosa: '))
area /= 3

while area >= 1:
    area -=18
    tinta +=1
print('''
    a quantidade de latas que devem ser compradas é de {}
    e o preço das latas ficou em ${}'''.format(tinta,tinta*80))        