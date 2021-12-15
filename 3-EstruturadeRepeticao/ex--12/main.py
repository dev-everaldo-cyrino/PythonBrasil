n = int(input('digite um numero: '))
num = [2,3,5,7,11]
if n in num:
    print('é primo')
elif n % 2 ==0 or n% 3 ==0 or n % 5 == 0 or n % 7 ==0:
    print('n é primo')
else: 
    print('é primo')