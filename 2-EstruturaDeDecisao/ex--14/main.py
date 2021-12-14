dt = input('coloque uma data no formato dd/mm/aaaa : ')
try:
    if dt[2] == '/' and dt[5] == '/':
            dia = int(dt[0]+dt[1])
            mes = int(dt[3]+dt[4])
            if dia > 31 or mes > 12:
                print('invalido, dia ou mes errados')
            else:
                print(' a data {} é valida !'.format(dt))
except:
    print(' a data é invalida !')