a = int(input('numero de habitantes da cidade A: '))
b = int(input('numero de habitantes da cidade B: '))
taxaa = 1.03
taxab = 1.015
ano = 0
if a > b:
    print('a cidade A ja passou a cidade B em numero de habitantes')
else:
    while a < b:
        a *= taxaa
        b *= taxab
        ano += 1
    print('''
          a cidade A com {:.0f} habitantes
          passou a cidade B com {:.0f} habitantes
          em exatos {} anos'''.format(a,b,ano))