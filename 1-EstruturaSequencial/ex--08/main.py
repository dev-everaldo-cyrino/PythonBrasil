arq = float(input('digite o tamanho do arquivo em MB: '))
vel = float(input('digite a velocidade da internet em MBps: '))
segundo = arq * vel
minuto = 0
if segundo > 60:
    while segundo > 60:
        segundo -= 60
        minuto += 1
print('''
o tempo de donwload de um arquivo de {} MB 
com uma internet de velocidade de {} MBps
é de exatos: {} minutos e {:.0f} segundos'''.format(arq,vel,minuto,segundo))