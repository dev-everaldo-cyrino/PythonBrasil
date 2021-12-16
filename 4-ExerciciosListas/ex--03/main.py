vogal = ['a','e','i','o','u']
consoante = []
n = input('digite uma palavra: ')
for x in n:
    if x in vogal:
        pass
    else:
        consoante.append(x)

print('''
      a palavra: {}
      tem: {} consoantes
      consoantes: {}'''.format(n,len(consoante),consoante))