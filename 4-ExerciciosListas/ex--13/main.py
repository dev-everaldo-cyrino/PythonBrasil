n = {"notas":[],"notas ao contrario":[],"soma":0,"notas acima da media":0,"abaixo de 7":0,"media":0}
print('digite quantas notas quiser, -1 encerra o programa')
while True:
    num = float(input('digite uma nota: '))
    if num == -1:
        break
    else:
        n["soma"]+=num
        n["notas"].append(num)
        if num < 7:
            n["abaixo de 7"]+=1
n["media"]=n["soma"]/len(n["notas"])
for x in range(1,len(n["notas"])+1):
    n["notas ao contrario"].append(n["notas"][-x])
    if n["notas"][-x] > n["media"]:
        n["notas acima da media"]+=1
print('Mostre a quantidade de valores que foram lidos; {}'.format(len(n["notas"])))
print('''Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
      {}'''.format(n["notas"]))
print('Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;')
for x in n["notas ao contrario"]:
    print(x)
print('''

Calcule e mostre a soma dos valores; {}
Calcule e mostre a média dos valores; {:.1f}
Calcule e mostre a quantidade de valores acima da média calculada; {}
Calcule e mostre a quantidade de valores abaixo de sete; {}
'''.format(n["soma"],n["media"],n["notas acima da media"],n["abaixo de 7"]))