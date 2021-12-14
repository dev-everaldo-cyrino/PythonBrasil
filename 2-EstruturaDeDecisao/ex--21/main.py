p1 = input('Telefonou para a vítima?(s/n): ')
p2 = input('Esteve no local do crime?(s/n): ')
p3 = input('Mora perto da vítima?(s/n): ')
p4 = input('Devia para a vítima?(s/n): ')
p5 = input('Já trabalhou com a vítima?(s/n): ')
p = [p1,p2,p3,p4,p5]
culpa = 0
for x in range(5):
    if p[x] == 's':
        culpa += 1
if culpa == 5:
    print('Assassino')
elif culpa == 3 or culpa ==4:
    print('Cúmplice')
elif culpa == 2:
    print('Suspeita')
else:
    print('Inocente')