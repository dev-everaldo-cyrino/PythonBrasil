num = int(input('numero: '))
li=[]
inicio = 0
def dados(inicio,li):
    li.append(inicio)
    for x in range(0,len(li)):
        li[x]+=1
    else:
        print(li)

while inicio < num: 
    dados(inicio,li)
    inicio+=1