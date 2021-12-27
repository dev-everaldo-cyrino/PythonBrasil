def  somaImposto(taxaImposto,altera):
    print('valor atual do produto R$ {}.00'.format(altera))
    taxaImposto = float(input('valor do importo em % : '))
    print('total: ',((taxaImposto/100)+1)*altera)
    altera = float(input('novo valor do produto: '))
    print('novo preço: ',((taxaImposto/100)+1)*altera)
somaImposto(10,100)