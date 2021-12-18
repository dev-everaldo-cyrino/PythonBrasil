n = {'total':[],'soma':0,'mult':1}
for x in range(1,6):
    n['total'].append(int(input('digite o {}° numero: '.format(x))))
    n['soma']+=n['total'][-1]
    n['mult']*=n['total'][-1]
else:
    print('''
          numeros: {}
          soma:    {}
          mult:    {}'''.format(n['total'],n['soma'],n['mult']))