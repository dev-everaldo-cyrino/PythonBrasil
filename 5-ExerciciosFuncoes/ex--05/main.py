n = {13:1,14:2,15:3,16:4,17:5,18:6,19:7,20:8,21:9,22:10,23:11}

while True:
    hora = int(input('hora: '))
    minutos = int(input('minutos: '))
    if hora < 0 or hora >23:
            break
    elif minutos < 0 or minutos > 60:
            break
    elif hora >12 and hora <24:
        print('a hora {}:{} pm passa a ser {}:{} pm'
        .format(hora,minutos,n[hora],minutos))
    else:
         print('a hora {}:{} am'.format(hora,minutos))
        