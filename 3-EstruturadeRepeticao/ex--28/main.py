n = input('numero: ')
num = ''
for x in range(1,len(n)+1):
  x *=-1
  num += num.join(n[x])
else:
  print(num)