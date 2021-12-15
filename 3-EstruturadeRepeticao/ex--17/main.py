n = int(input('digite um numero: '))
num = [1,2,3,5,7,11]
for x in range(n):
    x +=1
    if x in num:
        print('{} é primo'.format(x))   
    elif x % 2 ==0 or x% 3 ==0 or x % 5 == 0 or x % 7 ==0:
        pass
    else: 
        print('{} é primo'.format(x))