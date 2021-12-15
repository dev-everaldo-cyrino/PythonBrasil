op = int(input('quantas pessoas: '))
media = 0
for x in range(op):
    n = float(input('idade da {}° pessoa: '.format(x+1)))
    media +=n
media /= op
if media > 0 and media <25:
    print('a media da idade é {} , são jovens'.format(media))
elif media >=25 and media <60:
    print('a media da idade é {} , são adulta'.format(media))
elif media >= 60:
    print('a media da idade é {} , são idosa'.format(media))
