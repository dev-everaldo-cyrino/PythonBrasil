n = float(input('valor da divida: '))
num = {'3x':0.1,'6x':0.15,'9x':0.2,'12x':0.25}
print('''
Valor da Dívida     Valor dos Juros     Quantidade de Parcelas      Valor da Parcela
R$ {}             0  %                    1                        R$  {:.2f}
R$ {}             10 %                    3                        R$  {:.2f} 
R$ {}             15 %                    6                        R$  {:.2f}
R$ {}             20 %                    9                        R$  {:.2f}
R$ {}             25 %                   12                        R$  {:.2f}
'''.format(n,n,n+(n*num['3x']),n*num['3x'],n+(n*num['6x']),n*num['6x']
,n+(n*num['9x']),n*num['9x'],n+(n*num['12x']),n*num['12x']))