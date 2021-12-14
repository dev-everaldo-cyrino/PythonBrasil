num = []
total = 0
mult = 1
for x in range(4):
    num.append(float(input('digite a {}° nota: :'.format(x+1))))
    total += num[-1]
    mult *= num[-1]
    
num.sort()
print('''
      media: {:.2f}
      somando os numeros: {:.2f}
      multiplicando os numeros: {:.2f}
      o maior numero: {}
      o menor numero: {}'''.format(total / 4,total,mult,num[-1],num[0]))
