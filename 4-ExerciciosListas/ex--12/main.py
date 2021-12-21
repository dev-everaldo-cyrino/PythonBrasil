n = {'quest':["Telefonou para a vítima?","Esteve no local do crime?",
"Mora perto da vítima?","Devia para a vítima?","Já trabalhou com a vítima?",]
,'acertos':0, 'julgamento':["Inocente","Inocente","Suspeita","Cúmplice","Cúmplice","Assassino"]}
print('RESPONDA AS QUESTÕES COM (S OU N)')
for x in range(0,5):
    num = input('pergunta {} -- {}: '.format(x+1,n['quest'][x]))
    if num.upper() == 'S':
        n["acertos"]+=1
else:
    print('''
julgamento concluido.
o julgado respondeu sim para {} perguntras.
julgado: {}'''.format(n['acertos'],n["julgamento"][n["acertos"]]))