ano = int(input('digite um ano: '))
inicio = 1
bsexto = 0
n = 0
while inicio < ano:
    inicio +=1
    bsexto +=1
    if inicio % 100 == 0:
        bsexto -=1
    if inicio % 400 == 0:
        bsexto +=1
    if bsexto >= 4:
        bsexto = 0
        if inicio == ano:
            print('o ano {} é bissexto'.format(inicio))
            n = 1
if n == 0:
    print('o ano {} NÃO é bissexto !!'.format(ano))
            