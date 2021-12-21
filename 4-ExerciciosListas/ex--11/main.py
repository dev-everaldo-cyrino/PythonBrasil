n = {'mes':['janeiro','fevereiro','março','abril','maio','junho'
    ,'julho','agosto','setembro','outubro','novembro','dezembro']
     ,'temp':[] ,'media':0 ,'temp acima':0 ,'mesesaprovados':[]}
for x in range(0,12):
    n['temp'].append(float(input('temperatura do mês de {}: '.format(n['mes'][x]))))
    n['media']+=n['temp'][-1]
else:
    n['media'] /=12
    for x in range(0,12):
        if n['media'] > n['temp'][x]:
            pass
        else:
            n['mesesaprovados'].append(n['mes'][x]+': '+str(n['temp'][x]))
            n['temp acima']+=1
    else:
        print('''
media das temperaturas:
{:.2f}°
total de temperaturas acima da meida:
{}
meses com temperatura acima da media:
{}'''.format(n['media'],n['temp acima'],n['mesesaprovados']))