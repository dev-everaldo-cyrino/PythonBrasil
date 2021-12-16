li = []
media = 0
for x in range(1,5):
    li.append(float(input('digite a {}° nota: '.format(x))))
    media += li[-1]
print('''
      a nostas:
      {}
      a media:
      {:.1f}'''.format(li,media/len(li)))